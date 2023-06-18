import os
import pandas as pd
# from app.static.pythonscripts.csv import Csv
from app.static.pythonscripts.s3 import S3
from config import Configurations

config = Configurations().get_config()
config2 = Configurations().get_config2()

class Dataframes:

    def df_to_dict(self, df):
        df_dict = df.to_dict(orient='records')
        return df_dict

    def add_area(self, df):
        print('Dataframe.add_area')
        # df_areas = Csv().get_areas()
        df_areas = S3().get_s3_areas()
        df_merged = pd.merge(df, df_areas, on='area_identity', how='left')
        return df_merged

    def add_station(self, df):
        print('Dataframe.add_station')
        # df_stations = Csv().get_stations()
        df_stations = S3().get_s3_stations()
        df_merged = pd.merge(df, df_stations, on='station_identity', how='left')
        return df_merged

    def merge_dfs(self, df_1, df_2):
        print('Dataframe.merge_dfs')
        df_merged = pd.merge(df_1, df_2, how='left', on='pub_identity')
        return df_merged

    def append_df(self, _get, new_df):
        print('Dataframe: append_df')
        df_appended = pd.concat([_get, new_df], ignore_index=True)
        return df_appended

    def to_csv(self, df_appended, key):
        print('Dataframes: to_csv')
        # directory_path = os.getcwd()
        # directory_path = '/Users/andycarter/Documents/develop/thepubcrawls/'
        directory_path = config2['directory_path']
        print(directory_path)
        df_appended.to_csv(directory_path + '/files/' + config[key]['aws_key'], sep=',', encoding='utf-8', index=False)
