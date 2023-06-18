import json
import math
import pandas as pd
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
# from app.static.pythonscripts.csv import Csv
from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti

config = Configurations().get_config()


@app.route("/pub/areas")
def pub_areas():
    print('pub_areas')
    df = EntitiesMulti().get_pubs_reviews()
    pubs_reviews_json = Dataframes().df_to_dict(df)

    # df_areas = Csv().get_areas()
    df_areas = S3().get_s3_areas()
    areas_json = Dataframes().df_to_dict(df_areas)

    df_all = EntitiesMulti().get_pubs_reviews()
    df_all_area = df_all[['pub_name', 'area_identity']]
    df_all_area_group = df_all_area.groupby(['area_identity'], as_index=False).count()
    df_all_area_count = pd.merge(df_all_area_group, df_areas, how='left', on='area_identity') \
        .rename(columns={'pub_name': 'count'}).astype(str) \
        .sort_values(by=['area_latitude', 'area_longitude'], ascending=False)
    no_of_columns = 4

    no_of_records = df_all_area_count.shape[0]
    no_of_rows = math.ceil(no_of_records / no_of_columns)
    # print('no_of_rows: ' + str(no_of_rows))
    area_list = []
    df_full = pd.DataFrame()
    for y in range(no_of_rows):
        # print('y: ' + str(y))
        df_temp = df_all_area_count
        first_col = no_of_columns * y
        # print('first_col: ' + str(first_col))
        df_temp.sort_values(by=['area_latitude'], ascending=False, inplace=True)
        df_temp = df_temp.iloc[first_col:first_col + no_of_columns]
        # print(df_temp)
        df_temp_pos = df_temp.loc[df_temp['area_longitude'].astype(float) >= 0]
        df_temp_pos.sort_values(by=['area_longitude'], ascending=False, inplace=True)
        # print(df_temp_pos)
        df_temp_neg = df_temp.loc[df_temp['area_longitude'].astype(float) < 0]
        df_temp_neg.sort_values(by=['area_longitude'], ascending=False, inplace=True)
        # print(df_temp_neg)
        df_ordered = pd.concat([df_temp_neg, df_temp_pos])
        # print(df_ordered)
        df_full = pd.concat([df_full, df_ordered], ignore_index=True)
        # print(df_full)
        # area_temp_list = df_ordered.values.tolist()
        # area_list.append(area_temp_list)
        # break
    # print(df_full)

    areas_json = Dataframes().df_to_dict(df_full)

    # list_L = df[['area_latitude', 'area_longitude']].values.tolist()
    # _lat = []
    # _long = []
    # for l in list_L:
    #     _lat.append(l[0])
    #     _long.append(l[1])
    #
    # review_lat = sum(_lat) / len(_lat)
    # review_long = sum(_long) / len(_long)

    return render_template('pub_areas.html', areas=areas_json, pubs_reviews=pubs_reviews_json,
                           no_of_columns=no_of_columns, form_type='areas', no_of_rows=no_of_rows)\
        # ,
        #                    map_lat=review_lat, map_lng=review_long)
