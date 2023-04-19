import pandas as pd
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/crawl")
def pub_crawl():
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    df_stations = Functions().get_stations()
    df_all = Functions().get_pubs_reviews()
    df_all_x = df_all[['name', 'area_identity', 'place']]
    pub_list = df_all['name'].tolist()
    df_new_trunc = df_all[['name', 'station_identity']]
    df_new_count = df_new_trunc.groupby(['station_identity'], as_index=False).count()
    df_new_latlng = pd.merge(df_new_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'name': 'count'}).astype(str)\
        .sort_values(by='station')
    station_list = df_new_latlng['station'].tolist()
    all_json = Functions().df_to_dict(df_new_latlng)
    df_small = df_all[['name', 'place']].sort_values(by='name', ascending=False)
    place_list = df_small.values.tolist()

    df_area = Functions().get_areas()
    df_area_x = df_area[['area', 'area_identity']]
    df_pub_with_area = pd.merge(df_all_x, df_area_x, on='area_identity', how='left').sort_values(by='area')
    df_pub_area = df_pub_with_area[['place', 'name', 'area']]
    pub_area_list = df_pub_area.values.tolist()
    df_area_list = df_pub_with_area['area']

    df_unique = df_area_list.unique()
    list_pub_area = df_unique.tolist()
    range_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    return render_template('pub_crawl.html', google_key=config2['google_key'], pubs=all_json, pub_list=pub_list,
                           area_list=list_pub_area, pub_area=pub_area_list,
                           station_list=station_list, place_list=place_list, range_list=range_list)
