import json
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()


@app.route("/pub/list/<list_type>/<id_type>")
def pub_list(list_type, id_type):
    # if list_type == 'all':
    #     df = Functions().get_pubs_reviews().sort_values(by=['score'], ascending=False)
    #     heading = "All pubs"
    if id_type == 'True':
        df_scores = Functions().get_pubs_reviews()
        # filters = scores.loc[(scores['garden'] == True)]
        print(list_type.lower())
        df = df_scores.loc[(df_scores[list_type.lower()] == True)]
        # df = Functions().get_pubs_reviews().loc[Functions().get_pubs_reviews()[list_type.lower()] == True] \
        #     .sort_values(by=['rank'], ascending=False)
        heading = list_type
    elif id_type == 'all':
        df = Functions().get_pubs_reviews()
        heading = list_type
    else:
        df = Functions().get_pubs_reviews().loc[Functions().get_pubs_reviews()[list_type] == id_type]\
            .sort_values(by=['rank'], ascending=False)
        heading = id_type
    # print(df)
    pubs_reviews_json = Functions().df_to_dict(df)
    return render_template('pub_list.html', filter=heading, pubs_reviews=pubs_reviews_json, map_view=list_type,
                           map_lat=51.5, map_lng=-0.1, list_type=list_type, id_type=id_type)
