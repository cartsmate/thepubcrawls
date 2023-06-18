import pandas as pd
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.dataframes import Dataframes

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/map/all")
def pub_map():
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    df_all = EntitiesMulti().get_pubs_reviews()

    all_json = Dataframes().df_to_dict(df_all)


    df_stations = Csv().get_stations()
    # df_stations = S3().get_s3_stations()
    df_all_station = df_all[['pub_name', 'station_identity']]
    df_all_station_group = df_all_station.groupby(['station_identity'], as_index=False).count()
    df_all_station_count = pd.merge(df_all_station_group, df_stations, how='left', on='station_identity')\
        .rename(columns={'pub_name': 'count'}).astype(str)
    station_all_json = Dataframes().df_to_dict(df_all_station_count)

    df_areas = Csv().get_areas()
    # df_areas = S3().get_s3_areas()
    df_all_area = df_all[['pub_name', 'area_identity']]
    df_all_area_group = df_all_area.groupby(['area_identity'], as_index=False).count()
    df_all_area_count = pd.merge(df_all_area_group, df_areas, how='left', on='area_identity') \
        .rename(columns={'pub_name': 'count'}).astype(str)
    # \
    #     .drop('latitude', axis=1) \
    #     .drop('longitude', axis=1)
    # print(df_all_area_group)
    df_all_area = df_all[['pub_latitude', 'area_identity']]
    df_area_avg_lat = df_all_area.groupby(['area_identity'], as_index=False)['pub_latitude'].mean() \
        .rename(columns={'pub_latitude': 'avg_latitude'}).astype(str)
    df_lats = pd.merge(df_all_area_count, df_area_avg_lat, how='left', on='area_identity')
    # print(df_lats)
    df_all_area = df_all[['pub_longitude', 'area_identity']]
    df_area_avg_lng = df_all_area.groupby(['area_identity'], as_index=False)['pub_longitude'].mean() \
        .rename(columns={'pub_longitude': 'avg_longitude'}).astype(str)
    # print(df_area_avg_lng)
    df_lngs = pd.merge(df_lats, df_area_avg_lat, how='left', on='area_identity')
    # print(df_lngs)

    area_all_json = Dataframes().df_to_dict(df_all_area_count)
    print(config2)

    view = "all"
    list_L = df_all[['pub_latitude', 'pub_longitude']].values.tolist()
    _lat = []
    _long = []
    for l in list_L:
        _lat.append(l[0])
        _long.append(l[1])

    review_lat = sum(_lat) / len(_lat)
    review_long = sum(_long) / len(_long)
    print(review_lat)
    print(review_long)

    return render_template('pub_map.html', google_key=config2['google_key'],
                           full=all_json, station=station_all_json, area=area_all_json, form_type='map',
                           icon_hole=False, info_box=False, map_view=view, map_lat=review_lat, map_lng=review_long)
