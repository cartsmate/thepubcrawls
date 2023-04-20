import os
import json
import pandas as pd
from configparser import ConfigParser
from PIL import Image
from flask import render_template, redirect, url_for, g, session, request, flash
from app import app
from config import Configurations
from functions.functions import Functions
from werkzeug.utils import secure_filename

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
            df_pub = Functions().get_pub(pub_identity)
            pub_name = df_pub['name'].values[0].lower()
            print(pub_name)
            print('got here')
            filename = secure_filename(file.filename)
            print(filename)
            x, y = os.path.splitext(filename)
            print(y)
            fullfile = pub_name + y
            print(fullfile)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.getcwd() + '/app/static/images/venue/' + fullfile)
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
