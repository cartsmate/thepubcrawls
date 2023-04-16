import pandas as pd
from flask import render_template, request, url_for, g, redirect, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/map/reviewed")
def map_by_reviewed():
    if session.get('logged_in') != True:
        return redirect(url_for('login'))
    print('/pub/map/reviewed')
    df_stations = function.get_stations()

    df_all = function.get_pubs_reviews()
    df_reviewed = df_all.loc[df_all['colour'] != config['colour_new']]
    reviewed_json = function.df_to_dict(df_reviewed)
    df_reviewed_trunc = df_reviewed[['name', 'station_identity']]
    df_reviewed_count = df_reviewed_trunc.groupby(['station_identity'], as_index=False).count()
    df_reviewed_latlng = pd.merge(df_reviewed_count, df_stations, how='left', on='station_identity').rename(columns={'name': 'count'}).astype(str)
    df_reviewed_latlng['colour'] = config['colour_reviewed']
    station_reviewed_json = function.df_to_dict(df_reviewed_latlng)

    view = "reviewed"
    return render_template('pub_map_reviewed.html', google_key=config['google_key'],
                           full=reviewed_json, summary=station_reviewed_json,
                           icon_hole=False, info_box=False, map_view=view, map_lat=51.5, map_lng=-0.1)
