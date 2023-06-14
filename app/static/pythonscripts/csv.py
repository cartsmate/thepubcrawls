import os
import pandas as pd
from config import Configurations

config = Configurations().get_config()
config2 = Configurations().get_config2()


class Csv:

    def get_areas(self):
        df_areas = self.get_records('area')
        return df_areas

    def get_crawls(self):
        df_crawls = self.get_records('crawl')
        return df_crawls

    def get_photos(self):
        df_photos = self.get_records('photo')
        return df_photos

    def get_pubs(self):
        df_pubs = self.get_records('pub')
        return df_pubs

    def get_reviews(self):
        print('get_reviews')
        df_reviews = self.get_records('review')
        return df_reviews

    def get_stations(self):
        df_stations = self.get_records('station')
        return df_stations

    def get_records(self, aws_prefix):
        df = self.read_csv(aws_prefix)
        del_consol = aws_prefix + "_deletion"
        df_false = df.loc[df[del_consol] != True]
        return df_false

    def read_csv(self, prefix):
        # print('read_csv')
        directory_path = os.getcwd()
        directory_path = config2['directory_path']
        # directory_path = '/Users/andycarter/Documents/develop/thepubcrawls'
        obj_df = pd.read_csv(directory_path + 'files/' + prefix + 's.csv')
        return obj_df