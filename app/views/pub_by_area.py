from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/area/<area_id>")
def pub_by_area(area_id):
    print('/pub/area/<area_id>')
    df_pubs_by_area = function.get_pubs_by_area(area_id)
    pubs_rev_area_json = function.df_to_dict(df_pubs_by_area)
    view = "area"
    return render_template('pub_list.html', filter=area_id, pubs_reviews=pubs_rev_area_json, map_view=view,
                           map_lat=51.5, map_lng=-0.1)
