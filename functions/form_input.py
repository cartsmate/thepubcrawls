from flask import request
from config import Configurations

config = Configurations().get_config()


class FormInput:

    def get_pub(self, df_pubs, pub_id):
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'pub_deletion'] = request.form['pub_deletion']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'place'] = request.form['place']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'name'] = request.form['name']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'address'] = request.form['address']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'latitude'] = request.form['latitude']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'longitude'] = request.form['longitude']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'category'] = request.form['category']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'station_identity'] = request.form['station_identity']
        df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'area_identity'] = request.form['area_identity']
        return df_pubs

    def get_review(self, df_reviews, pub_id):
        if request.form.get('star') is None:
            star = ""
        else:
            star = request.form.get('star').lower()
        if request.form.get('reviewer') is None:
            reviewer = ""
        else:
            reviewer = request.form.get('reviewer').lower()
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'visit'] = "test date"
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
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'reviewer'] = reviewer
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'tv'] = True if request.form['tv'] == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'garden'] = True if request.form['garden'] == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'music'] = True if request.form['music'] == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'late'] = True if request.form['late'] == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'meals'] = True if request.form['meals'] == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'toilet'] = True if request.form['toilet'] == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'cheap'] = True if request.form['cheap'] == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'games'] = True if request.form['games'] == 'on' else False

        return df_reviews