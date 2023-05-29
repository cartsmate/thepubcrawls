import datetime
from flask import request
from config import Configurations

config = Configurations().get_config()


class FormInput:

    def get_pub(self, df_pubs, pub_id):
        print('FormInput: get_pub')
        print(request.form['pub_deletion'])
        print(request.form['place'])
        print(request.form['name'])
        print(request.form['address'])
        print(request.form['latitude'])
        print(request.form['longitude'])
        print(request.form['category'].lower())
        print(request.form['rank'])
        print(request.form['station_identity'])
        print(request.form['area_identity'])
        # df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'pub_deletion'] = request.form['pub_deletion']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'place'] = request.form['place']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'name'] = request.form['name']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'address'] = request.form['address']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'latitude'] = request.form['latitude']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'longitude'] = request.form['longitude']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'category'] = request.form['category'].lower()
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'rank'] = request.form['rank']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'station_identity'] = request.form['station_identity']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'area_identity'] = request.form['area_identity']
        return df_pubs

    def get_review(self, df_reviews, pub_id):
        print('FormInput: get_review')
        print(pub_id)
        # print(request.form.get('star'))
        # # print(request.form.get('reviewer').lower())
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
        if request.form.get('star') is None:
            star = ""
        else:
            star = request.form.get('star').lower()
        # if request.form.get('reviewer') is None:
        #     reviewer = ""
        # else:
        #     reviewer = request.form.get('reviewer').lower()
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'visit'] = datetime.datetime.now().strftime("%d/%m/%Y")
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'star'] = star
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'atmosphere'] = request.form['atmosphere']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'cleanliness'] = request.form['cleanliness']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'clientele'] = request.form['clientele']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'decor'] = request.form['decor']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'entertainment'] = request.form['entertainment']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'food'] = request.form['food']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'friendliness'] = request.form['friendliness']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'opening'] = request.form['opening']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'price'] = request.form['price']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'selection'] = request.form['selection']
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'rating'] = request.form['rating']
        # df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'reviewer'] = reviewer
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'pet'] = True if request.form.get('pet') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'tv'] = True if request.form.get('tv') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'garden'] = True if request.form.get('garden') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'music'] = True if request.form.get('music') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'late'] = True if request.form.get('late') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'meals'] = True if request.form.get('meals') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'toilets'] = True if request.form.get('toilets') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'cheap'] = True if request.form.get('cheap') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'games'] = True if request.form.get('games') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'quiz'] = True if request.form.get('quiz') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'pool'] = True if request.form.get('pool') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'lively'] = True if request.form.get('lively') == 'on' else False
        print(df_reviews.loc[df_reviews['pub_identity'] == pub_id])
        return df_reviews