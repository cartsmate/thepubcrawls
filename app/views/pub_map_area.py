import pandas as pd
from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/map/area")
def map_by_area():
    # print('/pub/map/area')
    df_stations = function.get_stations()
    df_areas = function.get_areas()

    df_all = function.get_pubs_reviews()
    all_json = function.df_to_dict(df_all)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity')\
        .rename(columns={'name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour_primary']
    station_all_json = function.df_to_dict(df_all_latlng)

    view = "all"
    return render_template('pub_map_all.html', google_key=config['google_key'],
                           full=all_json, summary=station_all_json,
                           icon_hole=False, info_box=False, map_view=view, map_lat=51.5, map_lng=-0.1)
