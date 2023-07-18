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
        review_val_list = [True if request.form.get('brunch') == 'on' else False,
                         True if request.form.get('dart') == 'on' else False,
                           request.form['detail'],
                         True if request.form.get('entertain') == 'on' else False,
                         True if request.form.get('favourite') == 'on' else False,
                         True if request.form.get('garden') == 'on' else False,
                         True if request.form.get('history') == 'on' else False,
                         True if request.form.get('late') == 'on' else False,
                         True if request.form.get('music') == 'on' else False,
                         True if request.form.get('pool') == 'on' else False,
                           pub_id,
                           True if request.form.get('quiz') == 'on' else False,
                         False,
                           uuid.uuid4(),
                         True if request.form.get('roast') == 'on' else False,
                         True if request.form.get('sport') == 'on' else False]

        review_attr_list = []
        for k, v in Review2().__dict__.items():
            review_attr_list.append(v.name)
        df_new_review = pd.DataFrame(columns=review_attr_list, data=[review_val_list])
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
