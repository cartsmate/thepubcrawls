import json
from flask import render_template, redirect, url_for, g, session, request
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.area.area import Area
from app.models.station.station import Station

config = Configurations().get_config()
config2 = Configurations().get_config2()


# @app.route("/pub/list/<list_type>/<id_type>")
# def pub_list(list_type, id_type):
@app.route("/pub/list/")
def pub_list():
    print('pub_list')
    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    ignore_list = ControlsList().get_control_lists()

    df_selection = EntitiesMulti().get_pubs_reviews()

    station = request.args.get('station')
    direction = request.args.get('direction')
    if request.args.get('station') != 'all':
        df_selection = df_selection.loc[df_selection['station_identity'] == station]
        print(df_selection)
        print(df_selection[['brunch', 'dart', 'entertain', 'favourite', 'garden', 'history', 'late', 'music', 'pool', 'quiz', 'roast', 'sport']])
        heading = df_selection.iloc[0]['station_name']
    elif request.args.get('direction') != 'all':
        heading = direction
        df_selection = df_selection.loc[df_selection['direction'] == direction]
    else:
        heading = 'All'

            # if list_type == 'all':
    #     df = Functions().get_pubs_reviews().sort_values(by=['score'], ascending=False)
    #     heading = "All pubs"
    # df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
    # print(df_pubs_reviews[['pub_name', 'station_name', 'direction']])
    # if id_type == 'True':
    #     df_scores = EntitiesMulti().get_pubs_reviews()
    #     # filters = scores.loc[(scores['garden'] == True)]
    #     # print(list_type.lower())
    #     df = df_scores.loc[(df_scores[list_type.lower()] == True)]
    #     # df = Functions().get_pubs_reviews().loc[Functions().get_pubs_reviews()[list_type.lower()] == True] \
    #     #     .sort_values(by=['rank'], ascending=False)
    #     heading = list_type
    # elif id_type == 'all':
    #     df = EntitiesMulti().get_pubs_reviews()
    #     heading = list_type
    # else:
    #     df = EntitiesMulti().get_pubs_reviews().loc[EntitiesMulti().get_pubs_reviews()[list_type] == id_type]\
    #         .sort_values(by=['rank'], ascending=False)
    #
    #     df = df.loc[(df[list_type] == id_type)]
    #     # df_pubs_reviews.loc[df_pubs_reviews[list_type] == id_type, 'colour'] = '#d9534f'
    #     # df_pubs_reviews.loc[df_pubs_reviews[list_type] != id_type, 'colour'] = '#0275d8'
    #
    #     heading = id_type
    # print(df)
    # df['colour'] = '#0275d8'

    review_list = {}
    # form_obj = {}
    for review in list(Review2().__dict__.keys()):
        if review not in ignore_list:
            # form_obj[review] = request.args.get(review)
            if request.args.get(review) == 'true':
                review_list[review] = ['True']
            else:
                review_list[review] = ['True', 'False']

    for review in review_list:
        df_selection = df_selection.loc[(df_selection[review].astype(str).isin(review_list[review]))]

    # if request.args.get('area') != "":
    #     filtered_values = filtered_values.loc[filtered_values['area_name'] == request.args.get('area')]

    # headers = list(filtered_values.columns)
    # print('headers')
    # print(headers)
    total_rows = df_selection.shape[0]
    pubs_reviews_json = Dataframes().df_to_dict(df_selection)




    # pubs_reviews_all_json = Dataframes().df_to_dict(df)
    # pubs_reviews_json = Dataframes().df_to_dict(df)

    # print(df)
    form_obj = {}
    for review in list(Review2().__dict__.keys()):
        if review not in ignore_list:
    #         print('df[review]')
    #         print(df[review])
    #         print('df[[review]]')
    #         print(df[[review]])
            df_unique = df_selection[review].unique()
    #         print('df_unique')
    #         print(df_unique)
            list_unique = df_unique.tolist()
    #         print('list_unique')
    #         print(list_unique)
            if True in list_unique:
                if False in list_unique:
                    form_obj[review] = 'some'
                else:
                    form_obj[review] = 'all'
            else:
                form_obj[review] = 'none'
    #             print('true')
    #             form_obj[review] = 'true'

    list_L = df_selection[['pub_latitude', 'pub_longitude']].values.tolist()
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
    inst_area = Area()
    inst_pub.__dict__.update(inst_area.__dict__)
    inst_station = Station()
    inst_pub.__dict__.update(inst_station.__dict__)
    inst_pub_review = inst_pub
    visible = {}
    for k, v in inst_pub_review.__dict__.items():
        visible[k] = v.table_visible

    return render_template('pub_list.html', filter=heading, pubs_reviews=pubs_reviews_json,
                           # pubs_reviews_all=pubs_reviews_all_json,
                           review_obj=Review2(),
                           map_lat=review_lat, map_lng=review_long, config2=config2,
                           # list_type=list_type, id_type=id_type,
                           form_type='list', google_key=config2['google_key'],
                           stations=stations_json, areas=areas_json,
                           visible=visible, headers=headers, icon_list=icon_list,
                           form_obj=form_obj,
                           station=station, direction=direction, total_rows=total_rows)
