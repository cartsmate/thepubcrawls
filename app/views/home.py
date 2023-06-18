import random

import botocore.exceptions
import pandas as pd
from flask import render_template
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.csv import Csv
from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.controls_list import ControlsList
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/home/")
def home():
    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, visible_list, icon_list, fields_list, ignore_list = ControlsList().get_control_lists()

    print(icon_list)
    if config2['env'] == 'prod':
        obj_df = S3().s3_read('counter_prod', ['pub_counter'])
    else:
        # directory_path = os.getcwd()
        # directory_path = '/Users/andycarter/Documents/develop/thepubcrawls/'
        directory_path = config2['directory_path']
        obj_df = pd.read_csv(directory_path + '/files/counter_qual.csv')
    obj_df["pub_counter"] = obj_df["pub_counter"] + 1

    if config2['env'] == 'prod':
        s3_resp = S3().s3_write(obj_df, 'counter_prod.csv')
    else:
        # directory_path = os.getcwd()
        # directory_path = '/Users/andycarter/Documents/develop/thepubcrawls/'
        directory_path = config2['directory_path']
        obj_df.to_csv(directory_path + '/files/counter_qual.csv', sep=',', encoding='utf-8', index=False)
    counter = str(obj_df["pub_counter"].values[0]).zfill(6)

    # directory_path = os.getcwd()
    # directory_path = '/Users/andycarter/Documents/develop/thepubcrawls/'
    directory_path = config2['directory_path']

    # try:
    df_pubs = S3().get_s3_pubs()
    df_pubs.to_csv(directory_path + '/files/pubs.csv', index=False, sep=',', encoding='utf-8')
    # print(df_pubs)

    df_reviews = S3().get_s3_reviews()
    df_reviews.to_csv(directory_path + '/files/reviews.csv', index=False, sep=',', encoding='utf-8')

    df_areas = S3().get_s3_areas()
    df_areas.to_csv(directory_path + '/files/areas.csv', index=False, sep=',', encoding='utf-8')

    df_crawls = S3().get_s3_crawls()
    df_crawls.to_csv(directory_path + '/files/crawls.csv', index=False, sep=',', encoding='utf-8')

    df_stations = S3().get_s3_stations()
    df_stations.to_csv(directory_path + '/files/stations.csv', index=False, sep=',', encoding='utf-8')

    df_photos = S3().get_s3_photos()
    df_photos.to_csv(directory_path + '/files/photos.csv', index=False, sep=',', encoding='utf-8')

    # except botocore.exceptions.EndpointConnectionError:
    #     df_pubs = Csv().get_pubs()
    #     df_reviews = Csv().get_reviews()
    #     df_areas = Csv().get_areas()
    #     df_crawls = Csv().get_crawls()
    #     df_photos = Csv().get_photos()

    df_all_area = df_pubs[['pub_name', 'area_identity']]
    # print(df_all_area)
    df_all_area_group = df_all_area.groupby(['area_identity'], as_index=False).count()
    # print(df_all_area_group)
    df_all_area_count = pd.merge(df_all_area_group, df_areas, how='left', on='area_identity') \
        .rename(columns={'pub_name': 'count'}).astype(str) \
        .sort_values(by=['count'], ascending=False)
    areas_json = Dataframes().df_to_dict(df_all_area_count)

    df_all_area_group2 = df_all_area.groupby(['area_identity'], as_index=False).count()
    # print(df_all_area_group2)
    df_all_area_count2 = pd.merge(df_all_area_group2, df_areas, how='left', on='area_identity')\
        .sort_values(by=['area_name'], ascending=True)
    # print(df_all_area_count2)
    areas_json2 = Dataframes().df_to_dict(df_all_area_count2)

    df_crawl_last = df_crawls.tail(1)
    # print(df_crawl_last)
    start = df_crawl_last['start'].values[0]
    # print(start)
    walk = df_crawl_last['walk'].apply(str).values[0]
    favourite = df_crawl_last['favourite'].values[0]
    stops = df_crawl_last['stops'].apply(str).values[0]
    criteria = df_crawl_last['criteria'].values[0]
    # df_pubs = Functions().get_pubs_reviews()
    df_pub = df_pubs.loc[df_pubs['place'] == start]
    df_pub['colour'] = '#d9534f'
    # print(df_pub)
    pub_json = Dataframes().df_to_dict(df_pub)

    df_pubs['colour'] = '#0275d8'
    pubs_json = Dataframes().df_to_dict(df_pubs)
    pubs_total = df_pubs.shape[0]
    # print('total: ' + str(pubs_total))
    random_identity = random.randint(0, pubs_total)
    # print('random: ' + str(pubs_random))
    pub_random = df_pubs.iloc[[random_identity]]
    df = pd.merge(pub_random, df_photos, how='left', on='pub_identity')
    photo_id = df['photo_identity'].values[0]
    # print(photo_id)
    # create random number
    # find index from random number in df_pubs
    # return single pub as random

    list_L = df_pubs[['pub_latitude', 'pub_longitude']].values.tolist()
    _lat = []
    _long = []
    for l in list_L:
        _lat.append(l[0])
        _long.append(l[1])

    review_lat = sum(_lat) / len(_lat)
    review_long = sum(_long) / len(_long)

    # g = geocoder.ip('me')
    # print(g.latlng)
    pub2 = Pub2()
    pub3 = pub2.__dict__
    # for k, v in Review2().__dict__.items():
    #     # print(k)
    #     print(v.name)
    #     print(v.alias)
    #     print(v.icon)

    # for p in pub2.__init__():
    #     p
    l1 = list(Review2().__dict__.keys())
    # for l in l1:
    #     print(l)
    ignore_list = ['review_deletion', 'review_identity', 'pub_identity', 'detail']

    l3 = [x for x in l1 if x not in ignore_list]

    return render_template('home.html', pubs_reviews=pubs_json, photo_array=config, map_view="stations",
                            map_lat=review_lat, map_lng=review_long, config=config, google_key=config2['google_key'],
                            row_loop=range(3), col_loop=range(4), areas=areas_json2, start=start,
                            walk=walk, favourite=favourite, stops=stops, criteria=criteria, photo_id=photo_id,
                            pubs=pubs_json, pub=pub_json, config2=config2, form_type='home', counter=counter,
                            ignore_list=ignore_list, review_obj=Review2(), features=l3, icon_list=icon_list)
