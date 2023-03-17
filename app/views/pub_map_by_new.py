import json
import pandas as pd
from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/map/new")
def map_by_new():
    print('/pub/map/new')
    # kwargs = json.loads(kwargs)
    # lat = kwargs['lat']
    # lng = kwargs['lng']
    # zoom = kwargs['zoom']

    df_stations = function.get_stations()

    df_all = function.get_pubs_reviews()

    df_new = df_all.loc[df_all['colour'] == config['colour_new']]
    new_json = function.df_to_dict(df_new)
    df_new_trunc = df_new[['name', 'station_identity']]
    df_new_count = df_new_trunc.groupby(['station_identity'], as_index=False).count()
    df_new_latlng = pd.merge(df_new_count, df_stations, how='left', on='station_identity').rename(columns={'name': 'count'}).astype(str)
    df_new_latlng['colour'] = config['colour_new']
    station_new_json = function.df_to_dict(df_new_latlng)

    view = "new"
    return render_template('pub_map.html', google_key=config['google_key'],
                           full=new_json, summary=station_new_json,
                           icon_hole=False, info_box=False, map_view=view)
