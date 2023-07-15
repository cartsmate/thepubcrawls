import json
import pandas as pd
import uuid
from flask import render_template, redirect, url_for, g, session, request
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.area.area import Area
from app.models.station.station import Station
from app.models.diary.week import Week

config = Configurations().get_config()
config2 = Configurations().get_config2()


# @app.route("/pub/list/<list_type>/<id_type>")
# def pub_list(list_type, id_type):
@app.route("/pub/day/")
def pub_day():
    print('pub_day')

    day = request.args.get('day')
    print('day: ' + day)
    directory_path = config2['directory_path']
    df_diary = pd.read_csv(directory_path + '/files/diary.csv')
    df_diary = df_diary.fillna('')
    df_diary_selected = df_diary.loc[df_diary[day] != '']
    df_diary_selected = df_diary_selected[['pub_identity', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]
    list_of_ids = df_diary_selected['pub_identity'].tolist()

    df_pubs_reviews = EntitiesMulti().get_pubs_reviews_stations()
    df_pubs = pd.read_csv(directory_path + '/files/pubs.csv')
    df_reviews = pd.read_csv(directory_path + '/files/reviews.csv')
    df_areas = pd.read_csv(directory_path + '/files/areas.csv')
    df_stations = pd.read_csv(directory_path + '/files/stations.csv')
    df = pd.merge(df_pubs, df_reviews, on='pub_identity', how='left')
    df1 = pd.merge(df, df_areas, on='area_identity', how='left')
    df2 = pd.merge(df1, df_stations, on='station_identity', how='left')
    df_selection = df2.loc[df2['pub_identity'].isin(list_of_ids)]
    df_all = pd.merge(df_selection, df_diary_selected, on='pub_identity', how='left')

    heading = 'Pubs on a ' + day

    inst_pub = Pub2()
    inst_review = Review2()
    inst_pub.__dict__.update(inst_review.__dict__)
    inst_area = Area()
    inst_pub.__dict__.update(inst_area.__dict__)
    inst_station = Station()
    inst_pub.__dict__.update(inst_station.__dict__)
    inst_pub_review = inst_pub
    visible = {}
    alias = {}
    for k, v in inst_pub_review.__dict__.items():
        if (k == 'station_name') and (request.args.get('station') != 'all'):
            visible[k] = False
        else:
            visible[k] = v.table_visible
        alias[k] = v.alias
    diary_headers = []
    diary_week = Week().__dict__.items()
    for k, v in diary_week:
        if k == day:
            visible[k] = True
        else:
            visible[k] = False
        alias[k] = k
    headers = list(df_all.columns)
    print(headers)
    print(visible)
    total_rows = df_selection.shape[0]
    pubs_selection_json = Dataframes().df_to_dict(df_all)
    return render_template('pub_day.html', form_type='day', total_rows=total_rows,
                           filter=heading, alias=alias,
                           visible=visible, headers=headers, pubs_selection=pubs_selection_json)
