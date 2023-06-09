import os
import pandas as pd
from flask import render_template, request
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


# @app.route("/pub/edit/<pub_id>")
# def pub_edit(pub_id):
@app.route("/pub/edit/")
def pub_edit():
    print('pub_edit')
    pub_id = request.args.get('pub_id')
    zoom = request.args.get('zoom')

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

    df_pub_review = EntitiesSingle().get_pub_review(pub_id)
    # selected_station = df_pub_review['station_identity'].values[0]

    df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
    # df_selection = df_pubs_reviews.loc[df_pubs_reviews['station_identity'] == selected_station]
    # station = selected_station
    # df_selection['colour'] = '#0275d8'
    # df_selection.loc[df_selection['pub_identity'] == pub_id, 'colour'] = '#d9534f'
    # pubs_reviews_json = Dataframes().df_to_dict(df_selection)

    # df_photos = pd.read_csv(os.getcwd() + '/files/photos.csv')
    # df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')
    # df_pub_photos.fillna('0', inplace=True)
    # df_pub_photos['colour'] = '#d9534f'
    # df_pub_photos.sort_values(by='pub_name', ascending=False)
    pubs_selected_json = Dataframes().df_to_dict(df_pub_review)

    df_areas = Csv().get_areas()
    areas_json = Dataframes().df_to_dict(df_areas)

    df_stations = Csv().get_stations()
    stations_json = Dataframes().df_to_dict(df_stations)

    review_lat = df_pub_review['pub_latitude'].values[0]
    review_long = df_pub_review['pub_longitude'].values[0]
    pubs_reviews_json = Dataframes().df_to_dict(df_pubs_reviews)
    return render_template('pub_read.html', form_type='edit', google_key=config2['google_key'],
                           pubs_selection=pubs_selected_json, config2=config2,
                           fields_list=fields_list, alias=alias,
                           stations=stations_json, areas=areas_json, config=config,
                           pubs_reviews=pubs_reviews_json,
                           # pubs_reviews=test_reviews,
                           map_lat=review_lat, map_lng=review_long, map_zoom=zoom,
                           star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                           check_list=check_list, slider_list=slider_list, date_list=date_list,
                           form_visible_list=form_visible_list, table_visible_list=table_visible_list,
                           required_list=required_list,
                           alias_list=alias_list, icon_list=icon_list,
                           review_obj=Review2(), ignore_list=ignore_list)
