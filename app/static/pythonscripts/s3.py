import io
import boto3
import pandas as pd
import numpy as np
from config import Configurations
from app.models.area.area import Area
from app.models.crawl.crawl import Crawl
from app.models.photo.photo import Photo
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.station.station import Station

config = Configurations().get_config()
config2 = Configurations().get_config2()


class S3:

    def get_s3_areas(self):
        df = self.get_s3_records('area', list(Area().__dict__.keys()))
        return df

    def get_s3_crawls(self):
        df = self.get_s3_records('crawl', list(Crawl().__dict__.keys()))
        return df

    def get_s3_photos(self):
        df = self.get_s3_records('photo', list(Photo().__dict__.keys()))
        return df

    def get_s3_pubs(self):
        # pubby = Pub2()
        df = self.get_s3_records('pub', list(Pub2().__dict__.keys()))
        # print(list(Pub2().__dict__.keys()))
        return df

    def get_s3_reviews(self):
        df = self.get_s3_records('review', list(Review2().__dict__.keys()))
        return df

    def get_s3_stations(self):
        df = self.get_s3_records('station', list(Station().__dict__.keys()))
        return df

    def get_s3_records(self, aws_prefix, list_of_columns):
        df = self.s3_read(aws_prefix, list_of_columns)
        del_consol = aws_prefix + "_deletion"
        df_false = df.loc[df[del_consol] != True]
        return df_false

    # def s3_read(self, prefix, list_of_columns):
    #     # print(prefix)
    #     # print(list_of_columns)
    #     # print('s3_read')
    #     s3 = boto3.resource('s3',
    #                         aws_access_key_id=config2['access_id'],
    #                         aws_secret_access_key=config2['access_key'])
    #     my_bucket = s3.Bucket(config2['bucket_name'])
    #     bucket_list = []
    #     for obj in my_bucket.objects.filter(Prefix=prefix):  # .all():
    #         if obj.key.find(".csv") != -1:
    #             bucket_list.append(obj.key)
    #     if len(bucket_list) == 1:
    #         list_of_objects = []  # Initializing empty list of dataframes
    #         for bucket in bucket_list:  # pubs.csv
    #             obj = s3.Object(config2['bucket_name'], bucket)
    #             data = obj.get()['Body'].read()
    #             list_of_objects.append(pd.read_csv(io.BytesIO(data), header=0, delimiter=",", low_memory=False))
    #         obj_df = pd.DataFrame(columns=list_of_columns)
    #         # print(obj_df)
    #         for obj in list_of_objects:
    #             temp_df = pd.DataFrame(data=obj)
    #             # print(temp_df)
    #             obj_df = pd.DataFrame(np.concatenate([obj_df.values, temp_df.values]), columns=obj_df.columns)
    #     else:
    #         obj_df = None
    #         print('error in processing')
    #     return obj_df
    #
    #
    # def s3_write(self, upload_object: object, s3_obj_name: object) -> object:
    #     client = boto3.client("s3", aws_access_key_id=config2['access_id'], aws_secret_access_key=config2['access_key'])
    #
    #     with io.StringIO() as csv_buffer:
    #         upload_object.to_csv(csv_buffer, index=False)
    #         response = client.put_object(Bucket=config2['bucket_name'], Key=s3_obj_name, Body=csv_buffer.getvalue())
    #         status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
    #         if status == 200:
    #             print(f"Successful {s3_obj_name} S3 put_object response. Status - {status}")
    #         else:
    #             print(f"Unsuccessful {s3_obj_name }S3 put_object response. Status - {status}")
    #
    #     # s3_resp = client.head_object(Bucket=config2['bucket_name'], Key=s3_obj_name)
    #
    #     return status
