import os
import json
import pandas as pd
from datetime import date
from datetime import datetime
from flask import render_template, redirect, url_for, g, session
from app import app
from ..models.pub import Pub
from ..models.review import Review
from ..models.photo import Photo
from config import Configurations
from functions.functions import Functions
from app.static.pythonscripts.form_new import FormNew

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/add/")
def pub_add():
    df_stations = Functions().get_stations()
    stations_json = Functions().df_to_dict(df_stations)
    areas_json = Functions().df_to_dict(Functions().get_records(config['area']['aws_prefix'], config['area']['model']))

    new_id = str(Functions().generate_uuid())
    df_pubs_reviews = Functions().get_pubs_reviews()

    pubs_reviews_json = Functions().df_to_dict(df_pubs_reviews)

    df_all = Functions().get_pubs_reviews()
    df_all['colour'] = '#0275d8'
    all_json = Functions().df_to_dict(df_all)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Functions().df_to_dict(df_all_latlng)
    parameter = ""

    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d")
    new_pub = Pub(pub_identity=new_id, pub_deletion=False, place="", name="", address="",
                  latitude=0, longitude=0, station_identity="", area_identity="", category="", rank=0)
    df_new_pub = pd.DataFrame([new_pub.__dict__])

    new_review = Review(review_identity=str(Functions().generate_uuid()), review_deletion=False, pub_identity=new_id,
                        visit=date_time_str, star="", atmosphere=0, cleanliness=0, clientele=0, decor=0,
                        entertainment=0, food=0, friendliness=0, opening=0, price=0, selection=0, rating=0, reviewer="",
                        pet=False, tv=False, garden=False, music=False, late=False, meals=False, toilets=False,
                        cheap=False, games=False, quiz=False, pool=False, lively=False)
    df_new_review = pd.DataFrame([new_review.__dict__])

    df_pub_review = pd.merge(df_new_pub, df_new_review, how="left", on="pub_identity")

    new_photo = Photo(pub_identity=new_id, photo_identity=str(Functions().generate_uuid()), photo_deletion=False)
    df_new_photo = pd.DataFrame([new_photo.__dict__])

    df_pub_photo = pd.merge(df_pub_review, df_new_photo, how='left', on='pub_identity')
    df_pub_photo['area'] = ""
    df_pub_photo['station'] = ""

    pub_json = Functions().df_to_dict(df_pub_photo)

    return render_template("pub_read.html", form_type='add', google_key=config2['google_key'],
                           new_id=new_id, config=config,
                           pub_review=pub_json,
                           stations=stations_json,
                           areas=areas_json,
                           pubs_reviews=pubs_reviews_json, full=all_json, summary=station_all_json)
