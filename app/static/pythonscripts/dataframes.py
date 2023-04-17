import os
import pandas as pd
from functions.functions import Functions
from config import Configurations

config = Configurations().get_config()


class Dataframes:

    def add_area(self, df):
        print('Dataframe.add_area')
        df_areas = Functions().get_areas()
        df_merged = pd.merge(df, df_areas, on='area_identity', how='left')
        return df_merged

    def add_station(self, df):
        print('Dataframe.add_area')
        df_stations = Functions().get_stations()
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
        df_appended.to_csv(os.getcwd() + '/files/' + config[key]['aws_key'], sep=',', encoding='utf-8', index=False)
