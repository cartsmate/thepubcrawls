import json
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/list/<list_type>/<id_type>")
def pub_list(list_type, id_type):
    # if list_type == 'all':
    #     df = Functions().get_pubs_reviews().sort_values(by=['score'], ascending=False)
    #     heading = "All pubs"
    df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
    if id_type == 'True':
        df_scores = EntitiesMulti().get_pubs_reviews()
        # filters = scores.loc[(scores['garden'] == True)]
        print(list_type.lower())
        df = df_scores.loc[(df_scores[list_type.lower()] == True)]
        # df = Functions().get_pubs_reviews().loc[Functions().get_pubs_reviews()[list_type.lower()] == True] \
        #     .sort_values(by=['rank'], ascending=False)
        heading = list_type
    elif id_type == 'all':
        df = EntitiesMulti().get_pubs_reviews()
        heading = list_type
    else:
        df = EntitiesMulti().get_pubs_reviews().loc[EntitiesMulti().get_pubs_reviews()[list_type] == id_type]\
            .sort_values(by=['rank'], ascending=False)

        df2 =df_pubs_reviews.loc[(df_pubs_reviews[list_type] == id_type)]
        # df_pubs_reviews.loc[df_pubs_reviews[list_type] == id_type, 'colour'] = '#d9534f'
        # df_pubs_reviews.loc[df_pubs_reviews[list_type] != id_type, 'colour'] = '#0275d8'

        heading = id_type
    # print(df)
    # df['colour'] = '#0275d8'
    pubs_reviews_all_json = Dataframes().df_to_dict(df2)
    # pubs_reviews_all_json = Dataframes().df_to_dict(df_pubs_reviews)
    pubs_reviews_json = Dataframes().df_to_dict(df)


    list_L = df[['pub_latitude', 'pub_longitude']].values.tolist()
    _lat = []
    _long = []
    for l in list_L:
        _lat.append(l[0])
        _long.append(l[1])

    review_lat = sum(_lat) / len(_lat)
    review_long = sum(_long) / len(_long)

    df_stations = Csv().get_stations()
    # df_stations = S3().get_s3_stations()
    df_areas = Csv().get_areas()
    # df_areas = S3().get_s3_areas()
    areas_json = Dataframes().df_to_dict(df_areas)
    stations_json = Dataframes().df_to_dict(df_stations)

    filtered_values = EntitiesMulti().get_pubs_reviews()

    headers = list(filtered_values.columns)

    inst_pub = Pub2()
    inst_review = Review2()
    inst_pub.__dict__.update(inst_review.__dict__)
    inst_pub_review = inst_pub
    visible = {}
    for k, v in inst_pub_review.__dict__.items():
        visible[k] = v.table_visible

    return render_template('pub_list.html', filter=heading, pubs_reviews=pubs_reviews_json, map_view=list_type,
                           pubs_reviews_all=pubs_reviews_all_json,
                           map_lat=review_lat, map_lng=review_long,
                           list_type=list_type, id_type=id_type,
                           form_type='list', google_key=config2['google_key'],
                           stations=stations_json, areas=areas_json,
                           visible=visible, headers=headers)
