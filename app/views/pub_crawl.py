from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/crawl")
def pub_crawl():
    print('/pub/crawl')
    df_all = function.get_pubs_reviews()
    all_json = function.df_to_dict(df_all)
    return render_template('pub_crawl.html', google_key=config['google_key'], pubs=all_json)
