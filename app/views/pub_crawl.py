from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/crawl")
def pub_crawl():
    print('/pub/crawl')
    return render_template('pub_crawl.html', google_key=config['google_key'])
