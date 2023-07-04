import pandas as pd
from datetime import datetime
from flask import render_template
from app import app
from app.models.pub.pub2 import *
from app.models.review.review2 import Review2
from app.models.area.area import Area
from app.models.photo.photo import Photo
from app.models.station.station import Station
from config import Configurations
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.uuid import Uuid

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/add/<lat>/<lng>")
def pub_add(lat, lng):
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
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, ignore_list = ControlsList().get_control_lists()

    df_all = EntitiesMulti().get_pubs_reviews()
    if lat == 'None' and lng == 'None':
        # print('lat and lng is NONE')
        list_L = df_all[['pub_latitude', 'pub_longitude']].values.tolist()
        _lat = []
        _long = []
        for l in list_L:
            _lat.append(l[0])
            _long.append(l[1])

        review_lat = sum(_lat) / len(_lat)
        review_long = sum(_long) / len(_long)
    else:
        # print('lat and lng RECEIVED')
        review_lat = lat
        review_long = lng
    df_stations = Csv().get_stations()
    # df_stations = S3().get_s3_stations()
    stations_json = Dataframes().df_to_dict(df_stations)
    # df_areas = S3().get_s3_areas()
    df_areas = Csv().get_areas()
    areas_json = Dataframes().df_to_dict(df_areas)

    new_id = str(Uuid().generate_uuid())
    df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
    df_pubs_reviews['colour'] = '#0275d8'
    pubs_reviews_json = Dataframes().df_to_dict(df_pubs_reviews)

    df_all['colour'] = '#0275d8'
    all_json = Dataframes().df_to_dict(df_all)
    df_all_trunc = df_all[['pub_name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'pub_name': 'count'}).astype(str)
    station_all_json = Dataframes().df_to_dict(df_all_latlng)
    parameter = ""

    pub_attr_list = []
    pub_val_list = []
    for k, v in Pub2().__dict__.items():
        pub_attr_list.append(v.name)
        pub_val_list.append(v.value)
    df_new_pub = pd.DataFrame(columns=pub_attr_list, data=[pub_val_list])

    review_attr_list = []
    review_val_list = []
    for k, v in Review2().__dict__.items():
        review_attr_list.append(v.name)
        review_val_list.append(v.value)
    df_new_review = pd.DataFrame(columns=review_attr_list, data=[review_val_list])

    df_pub_review = pd.merge(df_new_pub, df_new_review, how="left", on='pub_identity')
    pub_json = Dataframes().df_to_dict(df_pub_review)

    return render_template("pub_read.html", form_type='add', google_key=config2['google_key'],
                           config=config,
                           pub_review=pub_json, pubs_reviews=pubs_reviews_json, full=all_json, summary=station_all_json,
                           star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                           check_list=check_list, slider_list=slider_list, date_list=date_list,
                           alias_list=alias_list, icon_list=icon_list, alias=alias,
                           form_visible_list=form_visible_list,
                           table_visible_list=table_visible_list, required_list=required_list,
                           fields_list=fields_list,
                           stations=stations_json, areas=areas_json,
                           map_lat=review_lat, map_lng=review_long, review_obj=Review2(), ignore_list=ignore_list)
