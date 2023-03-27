import pandas as pd
from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/crawl")
def pub_crawl():
    print('/pub/crawl')
    df_stations = function.get_stations()
    df_all = function.get_pubs_reviews()
    pub_list = df_all['name'].tolist()
    df_new_trunc = df_all[['name', 'station_identity']]
    df_new_count = df_new_trunc.groupby(['station_identity'], as_index=False).count()
    df_new_latlng = pd.merge(df_new_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'name': 'count'}).astype(str)\
        .sort_values(by='station')
    # print(df_new_latlng)
    station_list = df_new_latlng['station'].tolist()
    all_json = function.df_to_dict(df_new_latlng)
    place_json = function.df_to_dict(df_all[['name', 'place']])
    df_small = df_all[['name', 'place', 'station', 'score']].sort_values(by='score', ascending=False)
    # place_list = df_all[['name', 'place']].tolist()
    place_list = df_small.values.tolist()

    range_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    return render_template('pub_crawl.html', google_key=config['google_key'], pubs=all_json, pub_list=pub_list,
                           station_list=station_list, place_list=place_list, range_list=range_list)
