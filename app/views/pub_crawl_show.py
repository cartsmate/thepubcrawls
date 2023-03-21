from flask import render_template, request
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/crawl/show", methods=['GET', 'POST'])
def pub_crawl_show():
    if request.method == 'GET':
        print('/pub/crawl/show: POST')
        start_inbound = request.form['start']
        print('start: ' + start_inbound)
        return render_template('pub_crawl_show.html', methods='get')
    if request.method == 'POST':
        print('/pub/crawl/show: POST')
        start = request.form['start']
        walk = request.form['walk']
        favourite = request.form['favourite']
        stops = request.form['stops']
        criteria = request.form['criteria']
        return render_template('pub_crawl_show.html', start=start, walk=walk, favourite=favourite, stops=stops,
                               criteria=criteria)
