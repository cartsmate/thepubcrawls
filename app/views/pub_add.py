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
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    df_stations = Functions().get_stations()
    stations_json = Functions().df_to_dict(df_stations)
    # stations_json = function.df_to_dict(function.get_records(config['source'], config['aws_prefix_station'],
    #                                                          json.loads(config['model_station'])))
    areas_json = Functions().df_to_dict(Functions().get_records(config['area']['aws_prefix'], config['area']['model']))

    new_pub_id = str(Functions().generate_uuid())
    date_now = date.today().strftime("%B %d, %Y")

    add_pub = Pub(pub_identity=new_pub_id, pub_deletion=False, place="", name="", address="", latitude=51.5,
                  longitude=-0.1, category="", station_identity="", area_identity="")

    add_review = Review(review_identity=str(Functions().generate_uuid()), pub_identity=new_pub_id, review_deletion=False,
                        visit=date_now, rank=0,
                        star="", atmosphere=0, cleanliness=0, clientele=0, decor=0, entertainment=0, food=0,
                        friendliness=0, opening=0, price=0, selection=0, reviewer="", tv=False, garden=False,
                        music=False, late=False, meals=False, toilets=False, cheap=False, games=False)
    df_pub_review = pd.merge(pd.DataFrame([add_pub.__dict__]), pd.DataFrame([add_review.__dict__]), on='pub_identity')
    df_pub_review['station'] = ""
    df_pub_review['area'] = ""
    df_pub_review['colour'] = config['colour']['reviewed']
    df_pub_review['score'] = 0
    pub_review_json = Functions().df_to_dict(df_pub_review)
    # print(pub_review_json)
    pubs_reviews_json = Functions().df_to_dict(Functions().get_pubs_reviews())

    df_all = Functions().get_pubs_reviews()
    all_json = Functions().df_to_dict(df_all)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity') \
        .rename(columns={'name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Functions().df_to_dict(df_all_latlng)

    return render_template("pub_add.html", form_type='add', google_key=config2['google_key'], pubs_reviews=pubs_reviews_json,
                           pub_review=pub_review_json, stations=stations_json, areas=areas_json,
                           full=all_json, summary=station_all_json, config=config)
                           # pub_review_fields=json.loads(config['column_all']),
                           # pub_fields=json.loads(config['column_pub']),
                           # review_fields=json.loads(config['column_review']),
                           # pub_visible=json.loads(config['visible_pub']),
                           # review_visible=json.loads(config['visible_review']),
                           # list_required=json.loads(config['column_required']),
                           # date_controls=json.loads(config['control_date']),
                           # input_controls=json.loads(config['control_input']),
                           # dropdown_controls=json.loads(config['control_dropdown']),
                           # slider_controls=json.loads(config['control_slider']),
                           # score_list=json.loads(config['column_score']))
