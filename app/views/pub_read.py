import os
import pandas as pd
from flask import render_template, request, redirect, url_for, g, session, flash
from app import app
from config import Configurations
from functions.functions import Functions
# from functions.form_input import FormInput
from app.static.pythonscripts.form_input import FormInput
from app.static.pythonscripts.form_new import FormNew
from app.static.pythonscripts.dataframes import Dataframes
from werkzeug.utils import secure_filename

config = Configurations().get_config()
config2 = Configurations().get_config2()

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/pub/<pub_id>", methods=['GET', 'POST'])
def pub_read(pub_id):
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    print('pub_read')
    df_pub_review = Functions().get_pub_review(pub_id)

    df_photos = pd.read_csv(os.getcwd() + '/files/photos.csv')
    print(df_photos)
    df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')
    print(df_pub_photos)
    pub_review_json = Functions().df_to_dict(df_pub_photos)

    # print(df_pub_review['rank'])
    if request.method == 'GET':
        print('pub_read: GET')
        return render_template("pub_read.html", form_type='read', google_key=config2['google_key'],
                               pub_review=pub_review_json, config=config)

    if request.method == 'POST':
        print('pub_read: POST')
        if df_pub_review.empty:
            print('new pub')
            df_pubs_reviews = Functions().get_pubs_reviews()
            if df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])].empty:
                print('new / not dupe pub')
                df_new_pub = FormNew().get_pub(pub_id)
                print('got new pub')
                df_pub_appended = Dataframes().append_df(Functions().get_pubs(), df_new_pub)
                # print(df_pub_appended)
                if df_pub_appended.shape[1] == len(config['pub']['model']):
                    Dataframes().to_csv(df_pub_appended, 'pub')
                    s3_resp = Functions().s3_write(df_pub_appended, config['pub']['aws_key'])
                else:
                    print('Error in processing')
                    # tkinter.messagebox.showwarning("Error in processing", "Failed to save new venue")
                    error = "Failed to save new venue"
                    flash(error)
                df_new_review = FormNew().get_review(pub_id)
                df_review_appended = Dataframes().append_df(Functions().get_reviews(), df_new_review)
                if df_review_appended.shape[1] == len(config['review']['model']):
                    Dataframes().to_csv(df_review_appended, 'review')
                    s3_resp = Functions().s3_write(df_review_appended, config['review']['aws_key'])
                else:
                    print('Error in processing')
                    # top = tkinter.Tk()
                    # top.geometry("150x150")
                    # tkinter.messagebox.showwarning("Error in processing", "Failed to save review")
                    # top.mainloop()
                    error = "Failed to save review"
                    flash(error)
                df_new_merged = Dataframes().merge_dfs(df_new_pub, df_new_review)
                df_area_added = Dataframes().add_area(df_new_merged)
                df_station_added = Dataframes().add_station(df_area_added)
                return render_template('pub_read.html', error=error, form_type='read', google_key=config2['google_key'],
                                       pub_review=Functions().df_to_dict(df_station_added), config=config)
            else:
                print('duplicate pub')
                df_pubs_reviews = Functions().get_pubs_reviews()
                dupe_id = df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])]['pub_identity']
                return redirect(url_for('pub_add'))
                # return render_template("pop_up_dupe.html",
                #                        pub_review=Functions().df_to_dict(
                #                            df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])]),
                #                        dupe_id=dupe_id)
        else:
            print('edit pub')
            df_pubs_updated = FormInput().get_pub(Functions().get_pubs(), pub_id)
            Dataframes().to_csv(df_pubs_updated, 'pub')
            s3_resp = Functions().s3_write(df_pubs_updated, config['pub']['aws_key'])

            df_review_updated = FormInput().get_review(Functions().get_reviews(), pub_id)
            Dataframes().to_csv(df_review_updated, 'review')
            s3_resp = Functions().s3_write(df_review_updated, config['review']['aws_key'])

            df_pub_review = Functions().get_pub_review(pub_id)

            df_photos = pd.read_csv(os.getcwd() + '/files/photos.csv')
            print(df_photos)
            df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')
            print(df_pub_photos)
            pub_review_json = Functions().df_to_dict(df_pub_photos)

            # print(df_pub_review)
            return render_template('pub_read.html', form_type='read', google_key=config2['google_key'],
                                   pub_review=pub_review_json, config=config)
