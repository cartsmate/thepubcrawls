import json
import pandas as pd
import uuid
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
from app.models.diary.week import Week

config = Configurations().get_config()
config2 = Configurations().get_config2()


# @app.route("/pub/list/<list_type>/<id_type>")
# def pub_list(list_type, id_type):
@app.route("/pub/list/")
def pub_list():
    print('pub_list')
    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    ignore_list, selected_pub_colour, other_pub_colour = ControlsList().get_control_lists()

    directory_path = config2['directory_path']

    show_other_pubs = True
    day = request.args.get('day')
    if day != 'all':
        show_other_pubs = False
    station = request.args.get('station')
    direction = request.args.get('direction')

    lat = request.args.get('lat')
    lng = request.args.get('lng')

    brunch = request.args.get('brunch')
    dart = request.args.get('dart')
    entertain = request.args.get('entertain')
    favourite = request.args.get('favourite')
    garden = request.args.get('garden')
    history = request.args.get('history')
    late = request.args.get('late')
    music = request.args.get('music')
    pool = request.args.get('pool')
    quiz = request.args.get('quiz')
    roast = request.args.get('roast')
    sport = request.args.get('sport')
    if brunch == True or dart == True or entertain == True or favourite == True or garden == True or history == True:
        show_other_pubs = False
    if late == True or music == True or pool == True or quiz == True or roast == True or sport == True:
        show_other_pubs = False

    # df_pubs_reviews = EntitiesMulti().get_pubs_reviews_stations()
    df_pubs = pd.read_csv(directory_path + '/files/pubs.csv')
    df_reviews = pd.read_csv(directory_path + '/files/reviews.csv')
    df_areas = pd.read_csv(directory_path + '/files/areas.csv')
    df_stations = pd.read_csv(directory_path + '/files/stations.csv')
    df_diary = pd.read_csv(directory_path + '/files/diary.csv')
    df_directions = pd.read_csv(directory_path + '/files/directions.csv')

    df_pb_rev = pd.merge(df_pubs, df_reviews, on='pub_identity', how='left')
    df_pb_rev_ara = pd.merge(df_pb_rev, df_areas, on='area_identity', how='left')
    df_pb_rev_ara_st = pd.merge(df_pb_rev_ara, df_stations, on='station_identity', how='left')
    df_pb_rev_ara_st_dry = pd.merge(df_pb_rev_ara_st, df_diary, on='pub_identity', how='left')
    df_pb_rev_ara_st_dry = df_pb_rev_ara_st_dry.fillna('')
    heading = "Pubs"
    # df2 = df[df['detail'].str.contains("music")]

    if station != 'all':
        # print(f'station: {station}')
        df_selection = df_pb_rev_ara_st_dry.loc[df_pb_rev_ara_st_dry['station_identity'] == station]
        station_name = df_stations.loc[df_stations['station_identity'] == station]['station_name'].values[0]
        full_heading = f'{station_name} {heading}'
        # print(df_selection)
    elif request.args.get('direction') != 'all':
        # print(f'direction: {direction}')
        df_selection = df_pb_rev_ara_st_dry.loc[df_pb_rev_ara_st_dry['direction_identity'] == direction]
        direction_name = df_directions.loc[df_directions['direction_identity'] == direction]['direction_name'].values[0]
        full_heading = f'{direction_name} {heading}'
    else:
        # df_selection = df_pb_rev_ara_st_dry
        full_heading = heading
        df_selection = df_pb_rev_ara_st_dry
    if day != 'all' and music == 'true':
        # print(f'music {music} on {day}')
        df_selection = df_selection[df_selection[day].str.contains('music')]
    if day != 'all' and quiz == 'true':
        # print(f'music {music} on {day}')
        df_selection = df_selection[df_selection[day].str.contains('quiz')]

    if day != 'all':
        df_selection = df_selection.loc[(df_selection[day] != '') & (df_selection[day] != 'Closed')]
        full_heading = f'{full_heading} on a {day}'

    review_list = {}
    pub_id = uuid.uuid4()
    for review in list(Review2().__dict__.keys()):
        if review not in ignore_list:
            if request.args.get(review) == 'true':
                review_list[review] = ['True']
            else:
                review_list[review] = ['True', 'False']
    for review in review_list:
        df_selection = df_selection.loc[(df_selection[review].astype(str).isin(review_list[review]))]

    # print(df_selection)
    df_selection['distance'] = 0
    headers = list(df_selection.columns)
    print(headers)
    inst_pub = Pub2()
    inst_review = Review2()
    inst_pub.__dict__.update(inst_review.__dict__)
    inst_area = Area()
    inst_pub.__dict__.update(inst_area.__dict__)
    inst_station = Station()
    inst_pub.__dict__.update(inst_station.__dict__)
    inst_pub_review = inst_pub
    visible = {}
    alias = {}

    for k, v in inst_pub_review.__dict__.items():
        # visible[k] = True
        if (k == 'station_name') and (request.args.get('station') != 'all'):
            visible[k] = False
        else:
            visible[k] = v.table_visible
        alias[k] = v.alias


    diary_week = Week().__dict__.items()
    for k, v in diary_week:
        # visible[k] = True
        if k == day:
            visible[k] = True
        else:
            visible[k] = False
        alias[k] = k
    alias['distance'] = 'distance'
    # visible_list = list(visible)
    # print(visible_list)
    # visible_order = visible_list.index('distance')

    if lat is not None:
        for index, row in df_selection.iterrows():
            lat_diff = abs(row['pub_latitude'] - float(lat))
            lng_diff = abs(row['pub_longitude'] - float(lng))
            tot_diff = lat_diff + lng_diff
            diff_rounded = round(tot_diff, 3)
            df_selection.loc[df_selection['pub_identity'] == row['pub_identity'], 'distance'] = diff_rounded
        df_selection = df_selection.sort_values(by='distance', ascending=True)
        df_selection = df_selection.head(10)
        df_selection['colour'] = '#0275d8'
        visible['distance'] = False

        visible_order = df_selection.columns.get_loc("distance")
        print(visible_order)
    else:
        df_selection['colour'] = '#0275d8'
        visible_order = df_selection.columns.get_loc("rank")
        visible['distance'] = False
        print(visible_order)

    pubs_selection_json = Dataframes().df_to_dict(df_selection)

    selection_id_list = df_selection['pub_identity'].tolist()
    df_non_selection = df_pb_rev_ara_st_dry.loc[~df_pb_rev_ara_st_dry['pub_identity'].isin(selection_id_list)]
    df_non_selection['colour'] = '#d9534f'

    pubs_reviews_json = Dataframes().df_to_dict(df_non_selection)

    form_obj = {}
    total_rows = df_selection.shape[0]

    if total_rows == 0:
        list_L = df_pb_rev_ara_st_dry[['pub_latitude', 'pub_longitude']].values.tolist()
        _lat = []
        _long = []
        for l in list_L:
            _lat.append(l[0])
            _long.append(l[1])
        review_lat = sum(_lat) / len(_lat)
        review_long = sum(_long) / len(_long)
    else:
        list_L = df_selection[['pub_latitude', 'pub_longitude']].values.tolist()
        _lat = []
        _long = []
        for l in list_L:
            _lat.append(l[0])
            _long.append(l[1])
        review_lat = sum(_lat) / len(_lat)
        review_long = sum(_long) / len(_long)

    # print(df_selection)
    for review in list(Review2().__dict__.keys()):
        if review not in ignore_list:
            df_unique = df_selection[review].unique()
            list_unique = df_unique.tolist()
            if True in list_unique:
                if False in list_unique:
                    form_obj[review] = 'some'
                else:
                    form_obj[review] = 'all'
            else:
                form_obj[review] = 'none'

    df_stations = Csv().get_stations()
    stations_json = Dataframes().df_to_dict(df_stations)
    df_areas = Csv().get_areas()
    areas_json = Dataframes().df_to_dict(df_areas)

    diary_headers = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    all_data_json = Dataframes().df_to_dict(df_pb_rev_ara_st_dry)
    return render_template('pub_list.html', form_type='list', filter=full_heading,
                           review_obj=Review2(pub_id), form_obj=form_obj,
                           pubs_reviews=pubs_reviews_json, pubs_selection=pubs_selection_json,
                           map_lat=review_lat, map_lng=review_long, config2=config2,
                           # map_zoom=zoom,
                           diary_headers=diary_headers, order=visible_order, all_data=all_data_json,
                           google_key=config2['google_key'], show_other_pubs=show_other_pubs,
                           visible=visible, alias=alias, headers=headers, icon_list=icon_list,
                           areas=areas_json, stations=stations_json,
                           station=station, direction=direction, day=day, total_rows=total_rows)
