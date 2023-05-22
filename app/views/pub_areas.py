import json
import math
import pandas as pd
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()


@app.route("/pub/areas")
def pub_areas():
    print('pub_areas')
    df = Functions().get_pubs_reviews()
    pubs_reviews_json = Functions().df_to_dict(df)

    df_areas = Functions().get_areas()
    areas_json = Functions().df_to_dict(df_areas)

    df_all = Functions().get_pubs_reviews()
    df_areas = Functions().get_areas()
    df_all_area = df_all[['name', 'area_identity']]
    df_all_area_group = df_all_area.groupby(['area_identity'], as_index=False).count()
    df_all_area_count = pd.merge(df_all_area_group, df_areas, how='left', on='area_identity') \
        .rename(columns={'name': 'count'}).astype(str) \
        .sort_values(by=['latitude', 'longitude'], ascending=False)
    no_of_columns = 4

    no_of_records = df_all_area_count.shape[0]
    no_of_rows = math.ceil(no_of_records / no_of_columns)

    area_list = []
    df_full = pd.DataFrame()
    for y in range(no_of_rows):
        print('y: ' + str(y))
        df_temp = df_all_area_count
        first_col = no_of_columns * y
        # print('first_col: ' + str(first_col))
        df_temp.sort_values(by=['latitude'], ascending=False, inplace=True)
        df_temp = df_temp.iloc[first_col:first_col + no_of_columns]
        # print(df_temp)
        df_temp_pos = df_temp.loc[df_temp['longitude'].astype(float) >= 0]
        df_temp_pos.sort_values(by=['longitude'], ascending=False, inplace=True)
        # print(df_temp_pos)
        df_temp_neg = df_temp.loc[df_temp['longitude'].astype(float) < 0]
        df_temp_neg.sort_values(by=['longitude'], ascending=False, inplace=True)
        # print(df_temp_neg)
        df_ordered = pd.concat([df_temp_neg, df_temp_pos])
        print(df_ordered)
        df_full = pd.concat([df_full, df_ordered], ignore_index=True)
        print(df_full)
        # area_temp_list = df_ordered.values.tolist()
        # area_list.append(area_temp_list)
        # break
    # print(df_full)

    areas_json = Functions().df_to_dict(df_full)

    return render_template('pub_areas.html', areas=areas_json, pubs_reviews=pubs_reviews_json,
                           no_of_columns=no_of_columns, form_type='areas')
