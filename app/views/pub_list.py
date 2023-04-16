import json
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()


@app.route("/pub/list/<list_type>/<id_type>")
def pub_list(list_type, id_type):
    if session.get('logged_in') != True:
        print('/pub/list/<list_type>/<id_type>')
        return redirect(url_for('login'))
    # df_pubs_reviews = function.get_pubs_reviews()
    # df_pubs_by_type = function.get_pubs_reviews().loc[function.get_pubs_reviews()[type] == id].sort_values(by=['score'], ascending=False)
    # kwargs = json.loads(kwargs)
    # list_type = kwargs['list_type']
    # id_type = kwargs['id_type']
    if list_type == 'all':
        pubs_reviews_json = Functions().df_to_dict(
            Functions().get_pubs_reviews().sort_values(by=['score'], ascending=False))
    else:
        pubs_reviews_json = Functions().df_to_dict(
            Functions().get_pubs_reviews().loc[Functions().get_pubs_reviews()[list_type] == id_type]
                .sort_values(by=['score'], ascending=False))
    # view = "area"
    return render_template('pub_list.html', filter=list_type, pubs_reviews=pubs_reviews_json, map_view=list_type,
                           map_lat=51.5, map_lng=-0.1, type=type, id=id)

#
# @app.route("/pub/list")
# def pub_list():
#     if not g.user:
#         print('/pub/map/all')
#         return redirect(url_for('login'))
#     # print('/pub/list')
#     pubs_reviews = function.get_pubs_reviews().sort_values(by=['score'], ascending=False)
#     pubs_reviews_json = function.df_to_dict(pubs_reviews)
#     view = "area"
#     # print(pubs_reviews_json)
#     return render_template('pub_list.html', filter="Full Listing", pubs_reviews=pubs_reviews_json, map_view=view,
#                            map_lat=51.5, map_lng=-0.1)
#
#
# @app.route("/pub/area/<area_id>")
# def pub_by_area(area_id):
#     print('/pub/area/<area_id>')
#     df_pubs_by_area = function.get_pubs_by_area(area_id)
#     pubs_rev_area_json = function.df_to_dict(df_pubs_by_area)
#     view = "area"
#     return render_template('pub_list.html', filter=area_id, pubs_reviews=pubs_rev_area_json, map_view=view,
#                            map_lat=51.5, map_lng=-0.1)
#
#
# @app.route("/pub/category/<cat_id>")
# def pub_by_category(cat_id):
#     print('/pub/category/<cat_id>')
#     df_pubs_by_category = function.get_pubs_by_category(cat_id)
#     pubs_rev_cat_json = function.df_to_dict(df_pubs_by_category)
#     view = "category"
#     return render_template('pub_list.html', filter=cat_id, pubs_reviews=pubs_rev_cat_json, map_view=view,
#                            map_lat=51.5, map_lng=-0.1)
#
#
# @app.route("/pub/star/<star_id>")
# def pub_by_star(star_id):
#     print('/pub/star/<star_id>')
#     df_pubs_by_star = function.get_pubs_by_star(star_id)
#     pubs_rev_star_json = function.df_to_dict(df_pubs_by_star)
#     view = "star"
#     return render_template('pub_list.html', filter=star_id, pubs_reviews=pubs_rev_star_json, map_view=view,
#                            map_lat=51.5, map_lng=-0.1)
#
#
# @app.route("/pub/station/<loc_id>")
# def pub_by_station(loc_id):
#     print('/pub/station/<loc_id>')
#     df_pubs_by_station = function.get_pubs_by_station(loc_id)
#     pubs_rev_loc_json = function.df_to_dict(df_pubs_by_station)
#     view = "station"
#     return render_template('pub_list.html', filter=loc_id, pubs_reviews=pubs_rev_loc_json, map_view=view, map_lat=51.5, map_lng=-0.1)
