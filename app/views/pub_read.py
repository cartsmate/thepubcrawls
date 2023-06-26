import os
import json
import pandas as pd
from flask import render_template, request, redirect, url_for, g, session, flash
from app import app
from config import Configurations
from app.static.pythonscripts.form_input import FormInput
from app.static.pythonscripts.form_new import FormNew
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.csv import Csv
from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.static.pythonscripts.entities_single import EntitiesSingle
from app.static.pythonscripts.controls_list import ControlsList
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.station.station import Station
from app.models.photo.photo import Photo
from app.models.area.area import Area
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

    directory_path = config2['directory_path']

    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, visible_list, icon_list, fields_list, ignore_list = ControlsList().get_control_lists()

    df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
    df_pubs_reviews['colour'] = '#0275d8'
    df_pubs_reviews.loc[df_pubs_reviews['pub_identity'] == pub_id, 'colour'] = '#d9534f'
    pubs_reviews_json = Dataframes().df_to_dict(df_pubs_reviews)
    print(df_pubs_reviews)

    df_pub_review = EntitiesSingle().get_pub_review(pub_id)
    print(df_pub_review)

    df_photos = pd.read_csv(os.getcwd() + '/files/photos.csv')
    print(df_photos)

    df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')
    df_pub_photos.fillna('0', inplace=True)
    df_pub_photos['colour'] = '#d9534f'
    pub_review_json = Dataframes().df_to_dict(df_pub_photos)
    print(df_pub_photos)

    # df_all = EntitiesMulti().get_pubs_reviews()
    # df_all['colour'] = '#0275d8'
    # df_all.loc[df_all['pub_identity'] == pub_id, 'colour'] = '#d9534f'
    # all_json = Dataframes().df_to_dict(df_all)
    df_stations = Csv().get_stations()
    # df_stations = S3().get_s3_stations()
    df_areas = Csv().get_areas()
    # df_areas = S3().get_s3_areas()
    areas_json = Dataframes().df_to_dict(df_areas)
    stations_json = Dataframes().df_to_dict(df_stations)
    df_all_trunc = df_pubs_reviews[['pub_name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'pub_name': 'count'}).astype(str)
    # df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Dataframes().df_to_dict(df_all_latlng)



    # print(df_pub_review['rank'])
    if request.method == 'GET':
        print('pub_read: GET')

        # list_L = df_pub_photos[['pub_latitude', 'pub_longitude']].values.tolist()
        # _lat = []
        # _long = []
        # for l in list_L:
        #     _lat.append(l[0])
        #     _long.append(l[1])

        review_lat = df_pub_photos['pub_latitude']
        review_long = df_pub_photos['pub_latitude']

        print(check_list)
        # print(df_pub_photos[['pet','tv','garden','music','late','meals','toilets','cheap','games','quiz','pool','lively']])
        return render_template("pub_read.html", form_type='read', google_key=config2['google_key'],
                               pub_review=pub_review_json, config=config, stations=stations_json, areas=areas_json,
                               full=pubs_reviews_json, summary=station_all_json, pubs_reviews=pubs_reviews_json,
                               map_lat=review_lat, map_lng=review_long,
                               fields_list=fields_list,
                               star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                               check_list=check_list, slider_list=slider_list, date_list=date_list,
                               visible_list=visible_list, required_list=required_list,
                               alias_list=alias_list, icon_list=icon_list,
                               review_obj=Review2(), ignore_list=ignore_list)

    if request.method == 'POST':
        print('pub_read: POST')
        if df_pub_review.empty:
            print('new pub')
            df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
            if df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])].empty:
                print('new / not dupe pub')

                df_new_pub = FormNew().get_pub(pub_id)
                print('got new pub')
                # df_pubs = S3().get_s3_pubs()
                df_pubs = Csv().get_pubs()
                df_pub_appended = Dataframes().append_df(df_pubs, df_new_pub)
                # print(df_pub_appended)
                error=""
                response = ""
                if df_pub_appended.shape[1] == len(Pub2().__dict__.items()):
                    Dataframes().to_csv(df_pub_appended, 'pub')
                    # s3_resp = S3().s3_write(df_pub_appended, 'pubs.csv')
                    # response = str(s3_resp)
                else:
                    print('Error in processing')
                    # tkinter.messagebox.showwarning("Error in processing", "Failed to save new venue")
                    error = "Failed to save new venue"
                    # flash(error)
                    response = str('pub error')
                df_new_review = FormNew().get_review(pub_id)
                # df_reviews = S3().get_s3_reviews()
                df_reviews = Csv().get_reviews()
                df_review_appended = Dataframes().append_df(df_reviews, df_new_review)
                if df_review_appended.shape[1] == len(Review2().__dict__.items()):
                    Dataframes().to_csv(df_review_appended, 'review')
                    # s3_resp = S3().s3_write(df_review_appended, 'reviews.csv')
                    # flash(s3_resp)
                    # response += " | " + str(s3_resp)
                else:
                    print('Error in processing')
                    # top = tkinter.Tk()
                    # top.geometry("150x150")
                    # tkinter.messagebox.showwarning("Error in processing", "Failed to save review")
                    # top.mainloop()
                    # error = "Failed to save review"
                    # flash(error)
                    response += " | " + str('review error')

                df_new_merged = Dataframes().merge_dfs(df_new_pub, df_new_review)
                df_area_added = Dataframes().add_area(df_new_merged)
                df_station_added = Dataframes().add_station(df_area_added)
                df_station_added['colour'] = '#d9534f'
                pd.set_option('display.max_columns', None)
                print(df_station_added)
                pub_review_json = Dataframes().df_to_dict(df_station_added)

                df_all = EntitiesMulti().get_pubs_reviews()
                df_all['colour'] = '#0275d8'
                df_all.loc[df_all['pub_identity'] == pub_id, 'colour'] = '#d9534f'
                pubs_reviews_json = Dataframes().df_to_dict(df_all)

                review_lat = df_station_added['pub_latitude']
                review_long = df_station_added['pub_longitude']
                flash(response)
                return render_template('pub_read.html', response=response,
                                       error=error, form_type='read', google_key=config2['google_key'],
                                       pubs_reviews=pubs_reviews_json, stations=stations_json, areas=areas_json,
                                       pub_review=pub_review_json, config=config,
                                       fields_list=fields_list,
                                       full=pubs_reviews_json, summary=station_all_json, map_lat=review_lat, map_lng=review_long,
                                       star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                                       check_list=check_list, slider_list=slider_list, date_list=date_list,
                                       visible_list=visible_list, required_list=required_list,
                                       alias_list=alias_list, icon_list=icon_list,
                                       review_obj=Review2(), ignore_list=ignore_list)
            else:
                print('duplicate pub')
                df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
                dupe_id = df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])]['pub_identity']
                return redirect(url_for('pub_add'))
                # return render_template("pop_up_dupe.html",
                #                        pub_review=Functions().df_to_dict(
                #                            df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])]),
                #                        dupe_id=dupe_id)
        else:
            print('edit pub')

            # df_pubs = S3().get_s3_pubs()
            df_pubs = Csv().get_pubs()
            df_pubs_updated = FormInput().get_pub(df_pubs, pub_id)
            df_pubs_updated.to_csv(directory_path + '/files/pubs.csv', index=False, sep=',', encoding='utf-8')
            # s3_resp = S3().s3_write(df_pubs_updated, config['pub']['aws_key'])
            # response = int(s3_resp)
            # print(response)

            # df_reviews = S3().get_s3_reviews()
            df_reviews = Csv().get_reviews()
            df_review_updated = FormInput().get_review(df_reviews, pub_id)
            df_review_updated.to_csv(directory_path + '/files/reviews.csv', index=False, sep=',', encoding='utf-8')
            # s3_resp = S3().s3_write(df_review_updated, config['review']['aws_key'])
            # response += int(s3_resp)
            # if response == 400:
            #     word_response = "Successfully updated"
            # else:
            #     word_response = "Error in processing"
            # print(word_response)

            df_pub_review = EntitiesSingle().get_pub_review(pub_id)

            df_photos = pd.read_csv(os.getcwd() + '/files/photos.csv')
            df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')
            df_pub_photos['colour'] = '#d9534f'
            df_pub_photos.fillna('0', inplace=True)
            pub_review_json = Dataframes().df_to_dict(df_pub_photos)

            # print(df_pub_review)
            df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
            pubs_reviews_json = Dataframes().df_to_dict(df_pubs_reviews)

            review_lat = df_pub_photos['pub_latitude']
            review_long = df_pub_photos['pub_longitude']
            # flash(word_response)

            return render_template('pub_read.html',
                                   # response=response,
                                   form_type='read', google_key=config2['google_key'],
                                   pub_review=pub_review_json, pubs_reviews=pubs_reviews_json, config=config,
                                   stations=stations_json, areas=areas_json,
                                   fields_list=fields_list,
                                   full=pubs_reviews_json, summary=station_all_json, map_lat=review_lat, map_lng=review_long,
                                   star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                                   check_list=check_list, slider_list=slider_list, date_list=date_list,
                                   visible_list=visible_list, required_list=required_list,
                                   alias_list=alias_list, icon_list=icon_list,
                                   review_obj=Review2(), ignore_list=ignore_list)
