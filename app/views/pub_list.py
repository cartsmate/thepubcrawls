import json
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


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
    df['colour'] = '#0275d8'
    pubs_reviews_json = Functions().df_to_dict(df)

    list_L = df[['latitude', 'longitude']].values.tolist()
    _lat = []
    _long = []
    for l in list_L:
        _lat.append(l[0])
        _long.append(l[1])

    review_lat = sum(_lat) / len(_lat)
    review_long = sum(_long) / len(_long)

    df_stations = Functions().get_stations()
    areas_json = Functions().df_to_dict(Functions().get_records(config['area']['aws_prefix'], config['area']['model']))
    stations_json = Functions().df_to_dict(df_stations)

    return render_template('pub_list.html', filter=heading, pubs_reviews=pubs_reviews_json, map_view=list_type,
                           map_lat=review_lat, map_lng=review_long, list_type=list_type, id_type=id_type,
                           form_type='list', google_key=config2['google_key'],
                           stations=stations_json, areas=areas_json,)
