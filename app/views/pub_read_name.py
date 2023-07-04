
from flask import render_template, request, redirect, url_for, g, session, flash
from app import app
from app.static.pythonscripts.csv import Csv

@app.route("/pub/name/<pub_name>", methods=['GET', 'POST'])
def pub_name_read(pub_name):
    print('pub_read_name')

    df_pubs = Csv().get_pubs()
    df_pub_selected = df_pubs.loc[df_pubs['pub_name'] == pub_name]
    pub_id = df_pub_selected.iloc[0]['pub_identity']

    return redirect(url_for('pub_read', pub_id=pub_id))
