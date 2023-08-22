import uuid
import pandas as pd
from flask import request
from config import Configurations
# from app.models.pub import *
from app.models.pub.place import Place
from app.models.pub.pub_identity import PubIdentity
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.diary.week import Week
from app.static.pythonscripts.uuid import Uuid

config = Configurations().get_config()


class FormNew:

    def get_pub(self, pub_id):
        new_pub = Pub2(pub_identity=pub_id, place=request.form['place'], pub_deletion=False,
                      pub_name=request.form['pub_name'], address=request.form['address'],
                      pub_latitude=request.form['pub_latitude'], pub_longitude=request.form['pub_longitude'],
                      station_identity=request.form['station_identity'],
                      area_identity=request.form['area_identity'], category=request.form['category'].lower(),
                      rank=request.form['rank'], colour=request.form['colour'])
        df_new_pub = pd.DataFrame([new_pub.__dict__])
        print('new pub from new: df_new_pub:')
        print(df_new_pub[['pub_identity', 'pub_name', 'pub_deletion']])
        return df_new_pub

    def get_review(self, pub_id):
        new_review = Review2(review_identity=uuid.uuid4(), review_deletion='false', pub_identity=pub_id,
                             brunch='true' if request.form.get('brunch') == 'on' else 'false',
                           dart='true' if request.form.get('dart') == 'on' else 'false',
                           entertain='true' if request.form.get('entertain') == 'on' else 'false',
                           favourite='true' if request.form.get('favourite') == 'on' else 'false',
                           garden='true' if request.form.get('garden') == 'on' else 'false',
                           history='true' if request.form.get('history') == 'on' else 'false',
                           late='true' if request.form.get('late') == 'on' else 'false',
                           music='true' if request.form.get('music') == 'on' else 'false',
                           pool='true' if request.form.get('pool') == 'on' else 'false',
                           quiz='true' if request.form.get('quiz') == 'on' else 'false',
                           roast='true' if request.form.get('roast') == 'on' else 'false',
                           sport='true' if request.form.get('sport') == 'on' else 'false')

        # review_attr_list = []
        # for k, v in Review2().__dict__.items():
        #     review_attr_list.append(v.name)
        # print('review_attr_list')
        # print(review_attr_list)
        # df_new_review = pd.DataFrame(columns=review_attr_list, data=[review_val_list])
        df_new_review = pd.DataFrame([new_review.__dict__])
        print('df_new_review')
        print(df_new_review)
        return df_new_review

    def get_diary(self, pub_id):
        new_week = Week(pub_identity=pub_id,
                          monday=request.form['monday'],
                          tuesday=request.form['tuesday'],
                          wednesday=request.form['wednesday'],
                          thursday=request.form['thursday'],
                          friday=request.form['friday'],
                          saturday=request.form['saturday'],
                          sunday=request.form['sunday'])
        df_new_week = pd.DataFrame([new_week.__dict__])
        print('new pub from new: df_new_pub:')
        print(df_new_week)
        return df_new_week
