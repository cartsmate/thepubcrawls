import os
import json
from configparser import ConfigParser
from flask import render_template, redirect, url_for
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()

@app.route("/admin")
def admin():
    print('/admin')
    df_areas = Functions().get_areas()
    df_pubs = Functions().get_pubs()

    for i, pub in df_pubs.iterrows():
        records = []
        for j, area in df_areas.iterrows():
            records.append([area.area, area.area_identity,
                            (abs(area['latitude'] - pub['latitude'])) + (abs(area['longitude'] - pub['longitude']))])
        records_sorted = sorted(records, key=lambda x: x[2])
        df_pubs.loc[df_pubs['pub_identity'] == pub['pub_identity'], 'area_identity'] = str(records_sorted[0][1])
    df_pubs.to_csv(os.getcwd() + '/files/venues.csv', sep=',', encoding='utf-8', index=False)
    s3_resp = Functions().s3_write(os.getcwd() + '/files/venues.csv', config['aws_key_pub'])
    return render_template('admin.html')
