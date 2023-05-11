import json
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()


@app.route("/pub/areas")
def pub_areas():

    df = Functions().get_pubs_reviews()
    pubs_reviews_json = Functions().df_to_dict(df)

    df_areas = Functions().get_areas()
    areas_json = Functions().df_to_dict(df_areas)

    return render_template('pub_areas.html', areas=areas_json, pubs_reviews=pubs_reviews_json)
