import pandas as pd
from flask import render_template, redirect, url_for, g
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/map/all")
def map_by_all():
    if not g.user:
        return redirect(url_for('login'))
    df_all = Functions().get_pubs_reviews()
    all_json = Functions().df_to_dict(df_all)

    df_stations = Functions().get_stations()
    df_all_station = df_all[['name', 'station_identity']]
    df_all_station_group = df_all_station.groupby(['station_identity'], as_index=False).count()
    df_all_station_count = pd.merge(df_all_station_group, df_stations, how='left', on='station_identity')\
        .rename(columns={'name': 'count'}).astype(str)
    df_all_station_count['colour'] = config['colour']['primary']
    station_all_json = Functions().df_to_dict(df_all_station_count)

    df_areas = Functions().get_areas()
    df_all_area = df_all[['name', 'area_identity']]
    df_all_area_group = df_all_area.groupby(['area_identity'], as_index=False).count()
    df_all_area_count = pd.merge(df_all_area_group, df_areas, how='left', on='area_identity')\
        .rename(columns={'name': 'count'}).astype(str)
    df_all_area_count['colour'] = config['colour']['red']
    area_all_json = Functions().df_to_dict(df_all_area_count)

    view = "all"
    return render_template('pub_map_all.html', google_key=config2['google_key'],
                           full=all_json, station=station_all_json, area=area_all_json,
                           icon_hole=False, info_box=False, map_view=view, map_lat=51.5, map_lng=-0.1)
