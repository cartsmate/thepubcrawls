import uuid
import pandas as pd
from flask import request
from config import Configurations
# from app.models.pub import *
from app.models.pub.place import Place
from app.models.pub.pub_identity import PubIdentity
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.static.pythonscripts.uuid import Uuid

config = Configurations().get_config()


class FormNew:

    def get_pub(self, pub_id):
        # new_pub = Pub2()
        #
        # for pub in list(Pub2().__dict__.keys()):
        #
        #     new_pub[pub] = request.form[pub]
        # new_pub.pub_identity = pub_id
        # return new_pub
        # place = Place(value=request.form['place'])

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
        # review_list = []
        # review_columns =

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
            # pub_val_list.append(v.value)
        df_new_review = pd.DataFrame(columns=review_attr_list, data=[review_val_list])

        # new_review = Review2(review_identity=Uuid().generate_uuid(), review_deletion=False,
        #                      pub_identity=PubIdentity(value=pub_id),
        #                     detail=request.form.get('detail'),
        #                     roast=True if request.form.get('roast') == 'on' else False,
        #                     sport=True if request.form.get('sport') == 'on' else False,
        #                     garden=True if request.form.get('garden') == 'on' else False,
        #                     music=True if request.form.get('music') == 'on' else False,
        #                     late=True if request.form.get('late') == 'on' else False,
        #                     brunch=True if request.form.get('brunch') == 'on' else False,
        #                     history=True if request.form.get('history') == 'on' else False,
        #                     dart=True if request.form.get('dart') == 'on' else False,
        #                     favourite=True if request.form.get('favourite') == 'on' else False,
        #                     quiz=True if request.form.get('quiz') == 'on' else False,
        #                     pool=True if request.form.get('pool') == 'on' else False,
        #                     entertain=True if request.form.get('entertain') == 'on' else False)
        # df_new_pub = pd.DataFrame([new_review.__dict__])
        return df_new_review
