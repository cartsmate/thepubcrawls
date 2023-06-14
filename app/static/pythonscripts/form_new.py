import pandas as pd
from flask import request
from config import Configurations
from app.models.pub.pub import Pub
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.static.pythonscripts.uuid import Uuid

config = Configurations().get_config()


class FormNew:

    def get_pub(self, pub_id):
        print('Form_new: get_pub')
        new_pub = Pub2(pub_identity=pub_id, place=request.form['place'], pub_deletion=request.form['pub_deletion'],
                      pub_name=request.form['pub_name'], address=request.form['address'],
                      pub_latitude=request.form['pub_latitude'], pub_longitude=request.form['pub_longitude'],
                      station_identity=request.form['station_identity'],
                      area_identity=request.form['area_identity'], category=request.form['category'].lower(),
                      rank=request.form['rank'])
        print(new_pub)
        df_new_pub = pd.DataFrame([new_pub.__dict__])
        return df_new_pub

    def get_review(self, pub_id):
        print('Form_new: get_review')
        # print(request.form.get('star'))
        # print(request.form.get('reviewer'))
        # print(request.form['atmosphere'])
        # print(request.form['cleanliness'])
        # print(request.form['clientele'])
        # print(request.form['decor'])
        # print(request.form['entertainment'])
        # print(request.form['food'])
        # print(request.form['friendliness'])
        # print(request.form['opening'])
        # print(request.form['price'])
        # print(request.form['selection'])
        # print(request.form['rating'])
        # print(request.form.get('pet'))
        # print(request.form.get('tv'))
        # print(request.form.get('garden'))
        # print(request.form.get('music'))
        # print(request.form.get('late'))
        # print(request.form.get('meals'))
        # print(request.form.get('toilets'))
        # print(request.form.get('cheap'))
        # print(request.form.get('games'))
        # print(request.form.get('quiz'))
        # print(request.form.get('pool'))
        # print(request.form.get('lively'))
        print('i am here')
        if request.form.get('star') is None:
            star = ""
        else:
            star = request.form.get('star').lower()
        # # if request.form.get('reviewer') is None:
        # #     reviewer = ""
        # # else:
        # #     reviewer = request.form.get('reviewer').lower()
        new_review = Review2(review_identity=Uuid().generate_uuid(), review_deletion=False, pub_identity=pub_id,
                            # visit=request.form['visit'],
                            # star=star,
                            # atmosphere=request.form['atmosphere'], cleanliness=request.form['cleanliness'],
                            # clientele=request.form['clientele'], decor=request.form['decor'],
                            # entertainment=request.form['entertainment'], food=request.form['food'],
                            # friendliness=request.form['friendliness'], opening=request.form['opening'],
                            # price=request.form['price'], selection=request.form['selection'],
                            # rating=request.form['rating'],
                            # reviewer="",
                            roast=True if request.form.get('roast') == 'on' else False,
                            sport=True if request.form.get('sport') == 'on' else False,
                            garden=True if request.form.get('garden') == 'on' else False,
                            music=True if request.form.get('music') == 'on' else False,
                            late=True if request.form.get('late') == 'on' else False,
                            brunch=True if request.form.get('brunch') == 'on' else False,
                            history=True if request.form.get('history') == 'on' else False,
                            dart=True if request.form.get('dart') == 'on' else False,
                            favourite=True if request.form.get('favourite') == 'on' else False,
                            quiz=True if request.form.get('quiz') == 'on' else False,
                            pool=True if request.form.get('pool') == 'on' else False,
                            entertain=True if request.form.get('entertain') == 'on' else False)
        df_new_pub = pd.DataFrame([new_review.__dict__])
        # df_new_pub = ""
        return df_new_pub
