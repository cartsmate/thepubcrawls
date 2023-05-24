import os
import json
import pandas as pd
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/edit/<pub_id>")
def pub_edit(pub_id):
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    df_all = Functions().get_pubs_reviews()
    df_all['colour'] = '#0275d8'
    df_all.loc[df_all['pub_identity'] == pub_id, 'colour'] = '#d9534f'
    all_json = Functions().df_to_dict(df_all)

    df_stations = Functions().get_stations()
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Functions().df_to_dict(df_all_latlng)

    df_pubs_reviews = Functions().get_pubs_reviews()
    df_pubs_reviews['colour'] = '#0275d8'
    pubs_reviews_json = Functions().df_to_dict(df_pubs_reviews)

    df_pub_review = Functions().get_pub_review(pub_id)
    df_photos = pd.read_csv(os.getcwd() + '/files/photos.csv')
    df_pub_photos = pd.merge(df_pub_review, df_photos, how='left', on='pub_identity')

    print(df_pub_photos)
    df_pub_photos.fillna(0)
    df_pub_photos['colour'] = '#d9534f'
    pub_review_json = Functions().df_to_dict(df_pub_photos)

    stations_json = Functions().df_to_dict(
        Functions().get_records(config['station']['aws_prefix'], config['station']['model']))
    areas_json = Functions().df_to_dict(Functions().get_records(config['area']['aws_prefix'], config['area']['model']))

    return render_template('pub_read.html', form_type='edit', google_key=config2['google_key'],
                           pub_review=pub_review_json,
                           stations=stations_json, areas=areas_json, config=config,
                           pubs_reviews=pubs_reviews_json, full=all_json, summary=station_all_json)
