import pandas as pd
from flask import request
from config import Configurations
from app.models.pub import Pub
from app.models.review import Review
from functions.functions import Functions

config = Configurations().get_config()


class FormNew:

    def get_pub(self, pub_id):
        print('Form_new: get_pub')
        new_pub = Pub(pub_identity=pub_id, pub_deletion=False, place=request.form['place'],
                      name=request.form['name'], address=request.form['address'],
                      latitude=request.form['latitude'], longitude=request.form['longitude'],
                      station_identity=request.form['station_identity'],
                      area_identity=request.form['area_identity'], category=request.form['category'].lower(),
                      rank=request.form['rank'])
        print(new_pub)
        df_new_pub = pd.DataFrame([new_pub.__dict__])
        return df_new_pub

    def get_review(self, pub_id):
        print('Form_new: get_review')
        print(request.form.get('star').lower())
        print(request.form.get('reviewer').lower())
        print(request.form['atmosphere'])
        print(request.form['cleanliness'])
        print(request.form['clientele'])
        print(request.form['decor'])
        print(request.form['entertainment'])
        print(request.form['food'])
        print(request.form['friendliness'])
        print(request.form['opening'])
        print(request.form['price'])
        print(request.form['selection'])
        print(request.form['rating'])
        print(request.form.get('pet'))
        print(request.form.get('tv'))
        print(request.form.get('garden'))
        print(request.form.get('music'))
        print(request.form.get('late'))
        print(request.form.get('meals'))
        print(request.form.get('toilets'))
        print(request.form.get('cheap'))
        print(request.form.get('games'))
        print(request.form.get('quiz'))
        print(request.form.get('pool'))
        print(request.form.get('lively'))
        print('i am here')
        if request.form.get('star') is None:
            star = ""
        else:
            star = request.form.get('star').lower()
        # # if request.form.get('reviewer') is None:
        # #     reviewer = ""
        # # else:
        # #     reviewer = request.form.get('reviewer').lower()
        new_review = Review(review_identity=Functions().generate_uuid(), review_deletion=False, pub_identity=pub_id,
                            visit=request.form['visit'],
                            star=star,
                            atmosphere=request.form['atmosphere'], cleanliness=request.form['cleanliness'],
                            clientele=request.form['clientele'], decor=request.form['decor'],
                            entertainment=request.form['entertainment'], food=request.form['food'],
                            friendliness=request.form['friendliness'], opening=request.form['opening'],
                            price=request.form['price'], selection=request.form['selection'],
                            rating=request.form['rating'],
                            reviewer="",
                            pet=True if request.form.get('pet') == 'on' else False,
                            tv=True if request.form.get('tv') == 'on' else False,
                            garden=True if request.form.get('garden') == 'on' else False,
                            music=True if request.form.get('music') == 'on' else False,
                            late=True if request.form.get('late') == 'on' else False,
                            meals=True if request.form.get('meals') == 'on' else False,
                            toilets=True if request.form.get('toilets') == 'on' else False,
                            cheap=True if request.form.get('cheap') == 'on' else False,
                            games=True if request.form.get('games') == 'on' else False,
                            quiz=True if request.form.get('quiz') == 'on' else False,
                            pool=True if request.form.get('pool') == 'on' else False,
                            lively=True if request.form.get('lively') == 'on' else False)
        df_new_pub = pd.DataFrame([new_review.__dict__])
        # df_new_pub = ""
        return df_new_pub
