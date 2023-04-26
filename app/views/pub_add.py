import json
import pandas as pd
from datetime import date
from flask import render_template, redirect, url_for, g, session
from app import app
from ..models.pub import Pub
from ..models.review import Review
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/add/")
def pub_add():
    df_stations = Functions().get_stations()
    stations_json = Functions().df_to_dict(df_stations)
    areas_json = Functions().df_to_dict(Functions().get_records(config['area']['aws_prefix'], config['area']['model']))

    new_id = str(Functions().generate_uuid())
    pubs_reviews_json = Functions().df_to_dict(Functions().get_pubs_reviews())

    df_all = Functions().get_pubs_reviews()
    all_json = Functions().df_to_dict(df_all)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Functions().df_to_dict(df_all_latlng)

    return render_template("pub_add.html", form_type='add', google_key=config2['google_key'],
                           pubs_reviews=pubs_reviews_json, new_id=new_id, config=config,
                           # pub_review=pub_review_json,
                           stations=stations_json,
                           areas=areas_json, full=all_json, summary=station_all_json)
