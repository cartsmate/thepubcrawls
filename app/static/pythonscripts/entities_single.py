import numpy as np
import pandas as pd
from config import Configurations
# from app.static.pythonscripts.csv import Csv
from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti

config = Configurations().get_config()


class EntitiesSingle:

    def get_record(self, dfs, id_code):
        df = dfs.loc[dfs['pub_identity'] == id_code]
        return df

    def get_pub_station(self, id_code):
        df_pub = self.get_pub(id_code)
        # df_stations = Csv().get_stations()
        df_stations = S3().get_s3_stations()
        # df_areas = Csv().get_areas()
        df_areas = S3().get_s3_areas()
        df_stations = df_stations[['station_identity', 'station_name']]
        df_areas = df_areas[['area_identity', 'area_name']]
        df_pub_station = pd.merge(df_pub, df_stations, how='left', on='station_identity')
        df_pub_area = pd.merge(df_pub_station, df_areas, how='left', on='area_identity')
        return df_pub_area

    def get_pub(self, id_code):
        df_pubs = S3().get_s3_pubs()
        df_pub = self.get_record(df_pubs, id_code)
        # print(df_pub)
        return df_pub

    def get_review(self, pub_id):
        # df_reviews = Csv().get_records('review')
        df_reviews = S3().get_s3_reviews()
        df_review = df_reviews.loc[df_reviews['pub_identity'] == pub_id]
        return df_review

    def get_pub_review(self, id_code):
        df_pub_review = pd.merge(self.get_pub_station(id_code), self.get_review(id_code), how='left', on='pub_identity')
        # df_pub_review['colour'] = np.where(df_pub_review['reviewer'] == 'BOTH',
        #                                    config['colour']['reviewed'],
        #                                    np.where(df_pub_review['reviewer'] == 'ANDY',
        #                                             config['colour']['reviewed'],
        #                                             np.where(df_pub_review['reviewer'] == 'AVNI',
        #                                                      config['colour']['reviewed'],
        #                                                      config['colour']['new'])))
        return df_pub_review

    def get_pubs_by_area(self, area_id):
        df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
        df_pubs_by_area = df_pubs_reviews.loc[df_pubs_reviews['area_name'] == area_id]
        return df_pubs_by_area

    def get_pubs_by_star(self, star_id):
        df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
        df_pubs_by_star = df_pubs_reviews.loc[df_pubs_reviews['star'] == star_id]
        return df_pubs_by_star

    def get_pubs_by_category(self, cat_id):
        df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
        df_pubs_by_category = df_pubs_reviews.loc[df_pubs_reviews['category'] == cat_id]
        return df_pubs_by_category

    def get_pubs_by_station(self, loc_id):
        df_pubs_reviews = EntitiesMulti().get_pubs_reviews()
        df_pubs_by_station = df_pubs_reviews.loc[df_pubs_reviews['station_name'] == loc_id]
        return df_pubs_by_station
