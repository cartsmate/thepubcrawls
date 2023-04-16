from flask import render_template, request, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/crawl/show", methods=['GET', 'POST'])
def pub_crawl_show():
    if session.get('logged_in') != True:
        return redirect(url_for('login'))
    if request.method == 'GET':
        print('/pub/crawl/show: POST')
        start_inbound = request.form['start']
        print('start: ' + start_inbound)
        return render_template('pub_crawl_show.html', methods='get')
    if request.method == 'POST':
        print('/pub/crawl/show: POST')

        try:
            station = request.form['station']
        except:
            station = "NONE"
        try:
            walk = request.form['walk']
        except:
            walk = "NONE"
        start = request.form['start']
        try:
            favourite = request.form['favourite']
        except:
            favourite = "NONE"
        stops = request.form['stops']
        try:
            criteria = request.form['criteria']
        except:
            criteria = "NONE"
        df_pubs = function.get_pubs_reviews()
        df_pub = df_pubs.loc[df_pubs['place'] == start]
        print(df_pub)
        pubs_json = function.df_to_dict(df_pubs)
        pub_json = function.df_to_dict(df_pub)
        return render_template('pub_crawl_show.html', google_key=config['google_key'], station=station, start=start,
                               walk=walk, favourite=favourite,
                               stops=stops, criteria=criteria, pubs=pubs_json, pub=pub_json)
