import pandas as pd
from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/map/")
def pub_map():
    print('/pub/map')
    df_stations = function.get_stations()

    df_all = function.get_pubs_reviews()
    all_json = function.df_to_dict(df_all)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity').rename(columns={'name': 'count'}).astype(str)
    station_all_json = function.df_to_dict(df_all_latlng)

    df_reviewed = df_all.loc[df_all['colour'] != config['colour_new']]
    reviewed_json = function.df_to_dict(df_reviewed)
    df_reviewed_trunc = df_reviewed[['name', 'station_identity']]
    df_reviewed_count = df_reviewed_trunc.groupby(['station_identity'], as_index=False).count()
    df_reviewed_latlng = pd.merge(df_reviewed_count, df_stations, how='left', on='station_identity').rename(columns={'name': 'count'}).astype(str)
    station_reviewed_json = function.df_to_dict(df_reviewed_latlng)

    df_new = df_all.loc[df_all['colour'] == config['colour_new']]
    new_json = function.df_to_dict(df_new)
    df_new_trunc = df_new[['name', 'station_identity']]
    df_new_count = df_new_trunc.groupby(['station_identity'], as_index=False).count()
    df_new_latlng = pd.merge(df_new_count, df_stations, how='left', on='station_identity').rename(columns={'name': 'count'}).astype(str)
    station_new_json = function.df_to_dict(df_new_latlng)

    view = "all"
    return render_template('pub_map.html', google_key=config['google_key'],
                           all_data=all_json, all_summary=station_all_json,
                           new_data=new_json, new_summary=station_new_json,
                           reviewed_data=reviewed_json, reviewed_summary=station_reviewed_json,
                           icon_hole=False, info_box=False, map_view=view, map_lat=51.5, map_lng=-0.1)
