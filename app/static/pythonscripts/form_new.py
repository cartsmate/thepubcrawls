import pandas as pd
from flask import request
from config import Configurations
from app.models.pub import Pub
from app.models.review import Review

config = Configurations().get_config()


class FormNew:

    def get_pub(self, pub_id):
        print('Form_new: get_pub')
        new_pub = Pub(pub_identity=pub_id, pub_deletion=request.form['pub_deletion'], place=request.form['place'],
                      name=request.form['name'], address=request.form['address'],
                      latitude=request.form['latitude'], longitude=request.form['longitude'],
                      station_identity=request.form['station_identity'],
                      area_identity=request.form['area_identity'], category=request.form['category'].lower())
        df_new_pub = pd.DataFrame([new_pub.__dict__])
        return df_new_pub

    def get_review(self, pub_id):
        print('Form_new: get_review')
        if request.form.get('star') is None:
            star = ""
        else:
            star = request.form.get('star').lower()
        if request.form.get('reviewer') is None:
            reviewer = ""
        else:
            reviewer = request.form.get('reviewer').lower()
        # print(request.form['review_identity'])
        # print(pub_id)
        # print(request.form['review_deletion'])
        # print(request.form['visit'])
        # print(star)
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
        # print(reviewer)
        # print(request.form.get('tv'))
        # print(request.form.get('garden'))
        # print(request.form.get('music'))
        # print(request.form.get('late'))
        # print(request.form.get('meals'))
        # print(request.form.get('toilets'))
        # print(request.form.get('cheap'))
        # print(request.form.get('games'))
        new_review = Review(review_identity=request.form['review_identity'], pub_identity=pub_id,
                            review_deletion=request.form['review_deletion'], visit=request.form['visit'], star=star,
                            atmosphere=request.form['atmosphere'], cleanliness=request.form['cleanliness'],
                            clientele=request.form['clientele'], decor=request.form['decor'],
                            entertainment=request.form['entertainment'], food=request.form['food'],
                            friendliness=request.form['friendliness'], opening=request.form['opening'],
                            price=request.form['price'], selection=request.form['selection'], reviewer=reviewer,
                            tv=True if request.form.get('tv') == 'on' else False,
                            garden=True if request.form.get('garden') == 'on' else False,
                            music=True if request.form.get('music') == 'on' else False,
                            late=True if request.form.get('late') == 'on' else False,
                            meals=True if request.form.get('meals') == 'on' else False,
                            toilets=True if request.form.get('toilets') == 'on' else False,
                            cheap=True if request.form.get('cheap') == 'on' else False,
                            games=True if request.form.get('games') == 'on' else False)
        # print('new_review')
        # print(new_review)
        df_new_pub = pd.DataFrame([new_review.__dict__])
        return df_new_pub
