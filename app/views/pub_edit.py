import os
import pandas as pd
from flask import render_template
from app import app
from config import Configurations
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.station.station import Station
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.static.pythonscripts.entities_single import EntitiesSingle
from app.static.pythonscripts.controls_list import ControlsList

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/edit/<pub_id>")
def pub_edit(pub_id):

    print('pub_edit')

    inst_pub = Pub2()
    inst_review = Review2()
    inst_pub.__dict__.update(inst_review.__dict__)
    inst_station = Station()
    inst_pub.__dict__.update(inst_station.__dict__)
    inst_pub_review = inst_pub
    alias = {}
    for k, v in inst_pub_review.__dict__.items():
        alias[k] = v.alias

    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    ignore_list = ControlsList().get_control_lists()

    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    df_all = EntitiesMulti().get_pubs_reviews()
    df_all['colour'] = '#0275d8'
    df_all.loc[df_all['pub_identity'] == pub_id, 'colour'] = '#d9534f'
    all_json = Dataframes().df_to_dict(df_all)

    df_stations = Csv().get_stations()
    # df_stations = S3().get_s3_stations()
    df_all_trunc = df_all[['pub_name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'pub_name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Dataframes().df_to_dict(df_all_latlng)

    df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
    df_pubs_reviews['colour'] = '#0275d8'
    pubs_reviews_json = Dataframes().df_to_dict(df_pubs_reviews)

    df_pub_review = EntitiesSingle().get_pub_review(pub_id)
    df_photos = pd.read_csv(os.getcwd() + '/files/photos.csv')
    df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')

    print(df_pub_photos)
    df_pub_photos.fillna('0', inplace=True)
    # if 'photo_identity' not in df_pub_photos.columns:
    #     df_pub_photos['photo_identity'] = '0'
    df_pub_photos['colour'] = '#d9534f'
    print(df_pub_photos)
    pub_review_json = Dataframes().df_to_dict(df_pub_photos)

    df_areas = Csv().get_areas()
    # df_areas = S3().get_s3_areas()
    stations_json = Dataframes().df_to_dict(df_stations)
    areas_json = Dataframes().df_to_dict(df_areas)

    # list_L = df_pub_photos[['latitude', 'longitude']].values.tolist()
    # _lat = []
    # _long = []
    # for l in list_L:
    #     _lat.append(l[0])
    #     _long.append(l[1])
    #
    # review_lat = sum(_lat) / len(_lat)
    # review_long = sum(_long) / len(_long)

    review_lat = df_pub_photos['pub_latitude']
    review_long = df_pub_photos['pub_longitude']

    return render_template('pub_read.html', form_type='edit', google_key=config2['google_key'],
                           pub_review=pub_review_json,
                           fields_list=fields_list, alias=alias,
                           stations=stations_json, areas=areas_json, config=config,
                           pubs_reviews=pubs_reviews_json, full=all_json, summary=station_all_json,
                           map_lat=review_lat, map_lng=review_long,
                           star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                           check_list=check_list, slider_list=slider_list, date_list=date_list,
                           form_visible_list=form_visible_list, table_visible_list=table_visible_list,
                           required_list=required_list,
                           alias_list=alias_list, icon_list=icon_list,
                           review_obj=Review2(), ignore_list=ignore_list)
