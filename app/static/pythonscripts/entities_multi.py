import numpy as np
import pandas as pd
from config import Configurations
# from app.static.pythonscripts.csv import Csv
from app.static.pythonscripts.s3 import S3

config = Configurations().get_config()


class EntitiesMulti:

    def get_pubs_station(self):
        # df_pubs = Csv().get_pubs()
        # df_stations = Csv().get_stations()
        # df_areas = Csv().get_areas()
        df_pubs = S3().get_s3_pubs()
        df_stations = S3().get_s3_stations()
        df_areas = S3().get_s3_areas()
        df_stations = df_stations[['station_identity', 'station_name']]
        df_areas = df_areas[['area_identity', 'area_name']]
        df_pubs_stations = pd.merge(df_pubs, df_stations, how='left', on='station_identity')
        df_pubs_areas = pd.merge(df_pubs_stations, df_areas, how='left', on='area_identity')
        return df_pubs_areas

    def get_pubs_area(self):
        # df_pubs = Csv().get_pubs()
        # df_areas = Csv().get_areas()
        df_pubs = S3().get_s3_pubs()
        df_areas = S3().get_s3_areas()
        df_stations = df_areas[['area_identity', 'area_name']]
        df_pubs_station = pd.merge(df_pubs, df_stations, how='left', on='area_identity')
        return df_pubs_station

    def get_pubs_new(self):
        # df_reviews = Csv().get_reviews()
        df_reviews = S3().get_s3_reviews()
        df_pubs_new = pd.merge(self.get_pubs_station(), df_reviews, how='left', on='pub_identity')
        df_pubs_new = df_pubs_new.loc[df_pubs_new['reviewer'] != 'BOTH']
        return df_pubs_new

    def get_pubs_reviews_areas(self):
        # df_reviews = Csv().get_reviews()
        df_reviews = S3().get_s3_reviews()
        df_pubs_reviews = pd.merge(self.get_pubs_station(), df_reviews, how='left', on='pub_identity')
        # df_pubs_reviews['score'] = round(df_pubs_reviews.loc[:, config['review']['score']].sum(axis=1) * 10)
        # df_pubs_reviews['colour'] = np.where(df_pubs_reviews['reviewer'] == 'BOTH',
        #                                      config['colour']['reviewed'],
        #                                      np.where(df_pubs_reviews['reviewer'] == 'ANDY',
        #                                               config['colour']['reviewed'],
        #                                               np.where(df_pubs_reviews['reviewer'] == 'AVNI',
        #                                                        config['colour']['reviewed'],
        #                                                        config['colour']['new'])))
        df_pubs_reviews.fillna(0, inplace=True)
        return df_pubs_reviews

    def get_pubs_reviews(self):
        # df_reviews = Csv().get_reviews()
        df_reviews = S3().get_s3_reviews()
        df_pubs_reviews = pd.merge(self.get_pubs_station(), df_reviews, how='left', on='pub_identity')
        df_pubs_reviews = df_pubs_reviews.loc[df_pubs_reviews['pub_deletion'] == 'False']
        # df_pubs_reviews['score'] = round(df_pubs_reviews.loc[:, config['review']['score']].mean(axis=1) * 10)
        df_pubs_reviews.fillna(False, inplace=True)
        # print(df_pubs_reviews[['name', 'pet', 'tv', 'garden', 'music', 'late', 'meals', 'toilets', 'cheap', 'games', 'quiz', 'pool', 'lively']])
        return df_pubs_reviews
