import pandas as pd
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/map/area")
def map_by_area():
    if session.get('logged_in') != True:
        return redirect(url_for('login'))
    # print('/pub/map/area')
    df_stations = Functions().get_stations()
    df_areas = Functions().get_areas()

    df_all = Functions().get_pubs_reviews()
    all_json = Functions().df_to_dict(df_all)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity')\
        .rename(columns={'name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Functions().df_to_dict(df_all_latlng)

    view = "all"
    return render_template('pub_map_all.html', google_key=config2['google_key'],
                           full=all_json, summary=station_all_json,
                           icon_hole=False, info_box=False, map_view=view, map_lat=51.5, map_lng=-0.1)
