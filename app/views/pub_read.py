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
    df_pubs_reviews = Functions().get_pubs_reviews()
    df_pubs_reviews['colour'] = '#0275d8'
    df_pubs_reviews.loc[df_pubs_reviews['pub_identity'] == pub_id, 'colour'] = '#d9534f'
    print(df_pubs_reviews)
    pubs_reviews_json = Functions().df_to_dict(df_pubs_reviews)

    df_pub_review = Functions().get_pub_review(pub_id)
    df_photos = pd.read_csv(os.getcwd() + '/files/photos.csv')
    df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')
    df_pub_photos = df_pub_photos.fillna('0')
    df_pub_photos['colour'] = '#d9534f'

    pub_review_json = Functions().df_to_dict(df_pub_photos)
    df_all = Functions().get_pubs_reviews()
    df_all['colour'] = '#0275d8'
    df_all.loc[df_all['pub_identity'] == pub_id, 'colour'] = '#d9534f'
    all_json = Functions().df_to_dict(df_all)
    df_stations = Functions().get_stations()
    areas_json = Functions().df_to_dict(Functions().get_records(config['area']['aws_prefix'], config['area']['model']))
    stations_json = Functions().df_to_dict(df_stations)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'name': 'count'}).astype(str)
    # df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Functions().df_to_dict(df_all_latlng)

    # print(df_pub_review['rank'])
    if request.method == 'GET':
        print('pub_read: GET')
        # print(df_pub_photos[['pet','tv','garden','music','late','meals','toilets','cheap','games','quiz','pool','lively']])
        return render_template("pub_read.html", form_type='read', google_key=config2['google_key'],
                               pub_review=pub_review_json, config=config, stations=stations_json, areas=areas_json,
                               full=all_json, summary=station_all_json, pubs_reviews=pubs_reviews_json)

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
                error=""
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
                df_station_added['colour'] = '#d9534f'
                pub_review_json = Functions().df_to_dict(df_station_added)
                return render_template('pub_read.html', error=error, form_type='read', google_key=config2['google_key'],
                                       pubs_reviews=pubs_reviews_json, stations=stations_json, areas=areas_json,
                                       pub_review=pub_review_json, config=config,
                                       full=all_json, summary=station_all_json)
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
            df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')
            df_pub_photos['colour'] = '#d9534f'
            pub_review_json = Functions().df_to_dict(df_pub_photos)

            # print(df_pub_review)
            return render_template('pub_read.html', form_type='read', google_key=config2['google_key'],
                                   pub_review=pub_review_json, config=config, stations=stations_json, areas=areas_json,
                                   full=all_json, summary=station_all_json)
