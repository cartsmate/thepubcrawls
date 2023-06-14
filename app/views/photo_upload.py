import os
import uuid
import pandas as pd
# from PIL import Image
from flask import render_template, redirect, url_for, request, flash
from app import app
from csv import writer
from config import Configurations
from app.models.photo.photo import Photo
from werkzeug.utils import secure_filename
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.entities_single import EntitiesSingle
from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.csv import Csv


UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

config = Configurations().get_config()
config2 = Configurations().get_config2()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route("/photo_upload/<pub_identity>", methods=['GET', 'POST'])
def photo_upload(pub_identity):
    # cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'GET':
        print('GET')
        return render_template('photo_upload.html', pub_identity=pub_identity)

    if request.method == 'POST':
        print('POST')
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        file = request.files['file']
        print(file)


        # if file.filename == '':
        #     flash('No image selected for uploading')
        #     return redirect(request.url)
        if file and allowed_file(file.filename):
        #
        #     print(file.filename)
            df_pub = EntitiesSingle().get_pub(pub_identity)
            pub_name = df_pub['name'].values[0].lower()
            print(pub_name)
            print('got here')
            filename = secure_filename(file.filename)
            print(filename)
            x, y = os.path.splitext(filename)
            print(y)
            fullfile = pub_name + y
            print(fullfile)
            new_name = uuid.uuid4()
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            new_photo = Photo(pub_identity=pub_identity, photo_identity=new_name, photo_deletion=False)
            df_new_photo = pd.DataFrame([new_photo.__dict__])
            df_photo_appended = Dataframes().append_df(Csv().get_photos(), df_new_photo)
            Dataframes().to_csv(df_photo_appended, 'photo')
            s3_resp = S3().s3_write(df_photo_appended, config['photo']['aws_key'])

            file.save(os.getcwd() + '/app/static/images/venue/' + str(new_name) + '.jpeg')
            new_row = [pub_identity, new_name, False]
            with open(os.getcwd() + '/files/photos.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(new_row)

            # print('upload_image filename: ' + filename)

            # img = Image.open(os.getcwd() + '/files/temp')
            # img.save(os.getcwd() + '/files/' + file.filename)
            # cursor.execute("INSERT INTO upload (title) VALUES (%s)", (filename,))
            # conn.commit()

            flash('Image successfully uploaded and displayed below')
            return redirect(url_for('pub_read', pub_id=pub_identity))
        else:
            print('got here next')
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return render_template('photo_upload.html')
