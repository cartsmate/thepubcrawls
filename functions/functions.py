import io
import os
import boto3
import uuid
import pandas as pd
import numpy as np
from config import Configurations

config = Configurations().get_config()
config2 = Configurations().get_config2()


class Functions:

    def df_to_dict(self, df):
        df_dict = df.to_dict(orient='records')
        return df_dict

    def get_photos(self):
        df_photos = self.get_records(config['photo']['aws_prefix'], config['photo']['model'])
        return df_photos

    def get_crawls(self):
        df_crawls = self.get_records(config['crawl']['aws_prefix'], config['crawl']['model'])
        return df_crawls

    def get_areas(self):
        df_areas = self.get_records(config['area']['aws_prefix'], config['area']['model'])
        return df_areas

    def get_records(self, aws_prefix, list_of_columns):
        df = self.read_csv(aws_prefix)
        if aws_prefix == 'venue':
            del_consol = 'pub' + "_deletion"
        elif aws_prefix == 'score':
            del_consol = 'review' + "_deletion"
        else:
            del_consol = aws_prefix + "_deletion"
        df_false = df.loc[df[del_consol] != True]
        return df_false

    def get_s3_records(self, aws_prefix, list_of_columns):
        df = self.s3_read(aws_prefix, list_of_columns)
        if aws_prefix == 'venue':
            del_consol = 'pub' + "_deletion"
        elif aws_prefix == 'score':
            del_consol = 'review' + "_deletion"
        else:
            del_consol = aws_prefix + "_deletion"
        df_false = df.loc[df[del_consol] != True]
        return df_false

    def get_s3_pubs(self):
        df = self.get_s3_records(config['pub']['aws_prefix'], config['pub']['model'])
        return df

    def get_s3_reviews(self):
        df = self.get_s3_records(config['review']['aws_prefix'], config['review']['model'])
        return df

    def get_s3_stations(self):
        df = self.get_s3_records(config['station']['aws_prefix'], config['station']['model'])
        return df

    def get_s3_areas(self):
        df = self.get_s3_records(config['area']['aws_prefix'], config['area']['model'])
        return df

    def get_s3_crawls(self):
        df = self.get_s3_records(config['crawl']['aws_prefix'], config['crawl']['model'])
        return df

    def get_s3_photos(self):
        df = self.get_s3_records(config['photo']['aws_prefix'], config['photo']['model'])
        return df

    def get_pubs(self):
        df_pubs = self.get_records(config['pub']['aws_prefix'], config['pub']['model'])
        return df_pubs

    def get_pubs_station(self):
        df_pubs = self.get_pubs()
        df_stations = self.get_stations()
        df_areas = self.get_areas()
        df_stations = df_stations[['station_identity', 'station']]
        df_areas = df_areas[['area_identity', 'area']]
        df_pubs_stations = pd.merge(df_pubs, df_stations, how='left', on='station_identity')
        df_pubs_areas = pd.merge(df_pubs_stations, df_areas, how='left', on='area_identity')
        return df_pubs_areas

    def get_pubs_area(self):
        df_pubs = self.get_pubs()
        df_areas = self.get_areas()
        df_stations = df_areas[['area_identity', 'area']]
        df_pubs_station = pd.merge(df_pubs, df_stations, how='left', on='area_identity')
        return df_pubs_station

    def get_pubs_by_area(self, area_id):
        df_pubs_reviews = self.get_pubs_reviews()
        df_pubs_by_area = df_pubs_reviews.loc[df_pubs_reviews['area'] == area_id]
        return df_pubs_by_area

    def get_pubs_by_star(self, star_id):
        df_pubs_reviews = self.get_pubs_reviews()
        df_pubs_by_star = df_pubs_reviews.loc[df_pubs_reviews['star'] == star_id]
        return df_pubs_by_star

    def get_pubs_by_category(self, cat_id):
        df_pubs_reviews = self.get_pubs_reviews()
        df_pubs_by_category = df_pubs_reviews.loc[df_pubs_reviews['category'] == cat_id]
        return df_pubs_by_category

    def get_pubs_by_station(self, loc_id):
        df_pubs_reviews = self.get_pubs_reviews()
        df_pubs_by_station = df_pubs_reviews.loc[df_pubs_reviews['station'] == loc_id]
        return df_pubs_by_station

    def get_reviews(self):
        print('get_reviews')
        df_reviews = self.get_records(config['review']['aws_prefix'], config['review']['model'])
        # print(df_reviews)
        return df_reviews

    def get_areas(self):
        df_areas = self.get_records(config['area']['aws_prefix'], config['area']['model'])
        return df_areas

    def get_stations(self):
        df_stations = self.get_records(config['station']['aws_prefix'], config['station']['model'])
        return df_stations

    def get_pubs_new(self):
        df_pubs_new = pd.merge(self.get_pubs_station(), self.get_reviews(), how='left', on='pub_identity')
        df_pubs_new = df_pubs_new.loc[df_pubs_new['reviewer'] != 'BOTH']
        return df_pubs_new

    def get_pubs_reviews_areas(self):
        df_pubs_reviews = pd.merge(self.get_pubs_station(), self.get_reviews(), how='left', on='pub_identity')
        df_pubs_reviews['score'] = round(df_pubs_reviews.loc[:, config['review']['score']].sum(axis=1) * 10)
        df_pubs_reviews['colour'] = np.where(df_pubs_reviews['reviewer'] == 'BOTH',
                                             config['colour']['reviewed'],
                                             np.where(df_pubs_reviews['reviewer'] == 'ANDY',
                                                      config['colour']['reviewed'],
                                                      np.where(df_pubs_reviews['reviewer'] == 'AVNI',
                                                               config['colour']['reviewed'],
                                                               config['colour']['new'])))
        df_pubs_reviews.fillna(0, inplace=True)
        return df_pubs_reviews

    def get_pubs_reviews(self):
        df_pubs_reviews = pd.merge(self.get_pubs_station(), self.get_reviews(), how='left', on='pub_identity')
        # df_pubs_reviews['score'] = round(df_pubs_reviews.loc[:, config['review']['score']].mean(axis=1) * 10)
        df_pubs_reviews.fillna(False, inplace=True)
        # print(df_pubs_reviews[['name', 'pet', 'tv', 'garden', 'music', 'late', 'meals', 'toilets', 'cheap', 'games', 'quiz', 'pool', 'lively']])
        return df_pubs_reviews

    def get_record(self, dfs, id_code):
        df = dfs.loc[dfs['pub_identity'] == id_code]
        return df

    def get_pub_station(self, id_code):
        df_pub = self.get_pub(id_code)
        df_stations = self.get_stations()
        df_areas = self.get_areas()
        df_stations = df_stations[['station_identity', 'station']]
        df_areas = df_areas[['area_identity', 'area']]
        df_pub_station = pd.merge(df_pub, df_stations, how='left', on='station_identity')
        df_pub_area = pd.merge(df_pub_station, df_areas, how='left', on='area_identity')
        return df_pub_area

    def get_pub(self, id_code):
        df_pub = self.get_record(self.get_records(config['pub']['aws_prefix'], config['pub']['model']), id_code)
        # print(df_pub)
        return df_pub

    def get_review(self, pub_id):
        df_reviews = self.get_records(config['review']['aws_prefix'], config['review']['model'])
        # print('df_reviews')
        # print(df_reviews)
        # print(pub_id)
        df_review = df_reviews.loc[df_reviews['pub_identity'] == pub_id]
        # print('df_review')
        # print(df_review)
        return df_review

    def get_pub_review(self, id_code):
        df_pub_review = pd.merge(self.get_pub_station(id_code), self.get_review(id_code), how='left', on='pub_identity')
        # df_pub_review['score'] = round(df_pub_review.loc[:, config['review']['score']].mean(axis=1) * 10)
        df_pub_review['colour'] = np.where(df_pub_review['reviewer'] == 'BOTH',
                                           config['colour']['reviewed'],
                                           np.where(df_pub_review['reviewer'] == 'ANDY',
                                                    config['colour']['reviewed'],
                                                    np.where(df_pub_review['reviewer'] == 'AVNI',
                                                             config['colour']['reviewed'],
                                                             config['colour']['new'])))
        return df_pub_review

    def generate_uuid(self):
        new_id = str(uuid.uuid4())
        return new_id

    def s3_write(self, upload_object: object, s3_obj_name: object) -> object:
        client = boto3.client("s3", aws_access_key_id=config2['access_id'], aws_secret_access_key=config2['access_key'])

        with io.StringIO() as csv_buffer:
            upload_object.to_csv(csv_buffer, index=False)
            response = client.put_object(Bucket=config2['bucket_name'], Key=s3_obj_name, Body=csv_buffer.getvalue())
            status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
            if status == 200:
                print(f"Successful {s3_obj_name} S3 put_object response. Status - {status}")
            else:
                print(f"Unsuccessful {s3_obj_name }S3 put_object response. Status - {status}")


        # client.put_object(Body=upload_object, Bucket=config2['bucket_name'], Key=s3_obj_name)

        # s3 = boto3.resource('s3')
        # s3.Bucket('bucketname').upload_file('/local/file/here.txt', 'folder/sub/path/to/s3key')

        # s3 = boto3.client('s3')
        # s3.upload_file(upload_object, config['bucket_name'], s3_obj_name)

        s3_resp = client.head_object(Bucket=config2['bucket_name'], Key=s3_obj_name)
        return s3_resp

    def read_csv(self, prefix):
        # print('read_csv')
        obj_df = pd.read_csv(os.getcwd() + '/files/' + prefix + 's.csv')
        return obj_df

    def s3_read(self, prefix, list_of_columns):
        # print('s3_read')
        s3 = boto3.resource('s3',
                            aws_access_key_id=config2['access_id'],
                            aws_secret_access_key=config2['access_key'])
        my_bucket = s3.Bucket(config2['bucket_name'])
        bucket_list = []
        for obj in my_bucket.objects.filter(Prefix=prefix):  # .all():
            if obj.key.find(".csv") != -1:
                bucket_list.append(obj.key)
        if len(bucket_list) == 1:
            list_of_objects = []  # Initializing empty list of dataframes
            for bucket in bucket_list:  # pubs.csv
                obj = s3.Object(config2['bucket_name'], bucket)
                data = obj.get()['Body'].read()
                list_of_objects.append(pd.read_csv(io.BytesIO(data), header=0, delimiter=",", low_memory=False))
            obj_df = pd.DataFrame(columns=list_of_columns)
            for obj in list_of_objects:
                temp_df = pd.DataFrame(data=obj)
                obj_df = pd.DataFrame(np.concatenate([obj_df.values, temp_df.values]), columns=obj_df.columns)
        else:
            obj_df = None
            print('error in processing')
        return obj_df
