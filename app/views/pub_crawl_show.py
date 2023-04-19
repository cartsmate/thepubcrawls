from flask import render_template, request, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/crawl/show", methods=['GET', 'POST'])
def pub_crawl_show():
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    if request.method == 'GET':
        print('/pub/crawl/show: POST')
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
        df_pubs = Functions().get_pubs_reviews()
        df_pub = df_pubs.loc[df_pubs['place'] == start]
        pubs_json = Functions().df_to_dict(df_pubs)
        pub_json = Functions().df_to_dict(df_pub)
        return render_template('pub_crawl_show.html', google_key=config2['google_key'], station=station, start=start,
                               walk=walk, favourite=favourite,
                               stops=stops, criteria=criteria, pubs=pubs_json, pub=pub_json)
