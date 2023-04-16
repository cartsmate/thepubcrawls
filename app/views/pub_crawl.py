import pandas as pd
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/crawl")
def pub_crawl():
    if session.get('logged_in') != True:
        return redirect(url_for('login'))
    df_stations = Functions().get_stations()
    df_all = Functions().get_pubs_reviews()
    pub_list = df_all['name'].tolist()
    df_new_trunc = df_all[['name', 'station_identity']]
    df_new_count = df_new_trunc.groupby(['station_identity'], as_index=False).count()
    df_new_latlng = pd.merge(df_new_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'name': 'count'}).astype(str)\
        .sort_values(by='station')
    station_list = df_new_latlng['station'].tolist()
    all_json = Functions().df_to_dict(df_new_latlng)
    df_small = df_all[['name', 'place', 'station', 'score']].sort_values(by='score', ascending=False)
    place_list = df_small.values.tolist()

    range_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    return render_template('pub_crawl.html', google_key=config2['google_key'], pubs=all_json, pub_list=pub_list,
                           station_list=station_list, place_list=place_list, range_list=range_list)
