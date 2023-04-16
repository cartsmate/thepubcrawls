import json
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/edit/<pub_id>")
def pub_edit(pub_id):
    if session.get('logged_in') != True:
        return redirect(url_for('login'))
    stations_json = Functions().df_to_dict(
        Functions().get_records(config['station']['aws_prefix'], config['station']['model']))
    areas_json = Functions().df_to_dict(Functions().get_records(config['area']['aws_prefix'], config['area']['model']))
    return render_template('pub_edit.html', form_type='edit', google_key=config2['google_key'],
                           pub_review=Functions().df_to_dict(Functions().get_pub_review(pub_id)),
                           stations=stations_json, areas=areas_json, config=config)
