from flask import request
from config import Configurations
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.static.pythonscripts.controls_list import ControlsList
config = Configurations().get_config()


class FormInput:

    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
        required_list, visible_list, icon_list, fields_list, ignore_list = ControlsList().get_control_lists()

    def get_pub(self, df_pubs, pub_id):
        for pub in list(Pub2().__dict__.keys()):
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, pub] = request.form[pub]
        return df_pubs

    def get_review(self, df_reviews, pub_id):
        print('FormInput: get_review')
        # for review in list(Review2().__dict__.keys()):
        #     if review not in self.ignore_list:
        #         print(review)
        #         df_reviews.loc[df_reviews['pub_identity'] == pub_id, review] = True if request.form.get(review) == 'on' else False
        print('roast')
        print(df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'roast'])
        print('value')
        print(request.form.get('roast'))

        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'brunch'] = True if request.form.get('brunch') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'dart'] = True if request.form.get('dart') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'entertain'] = True if request.form.get('entertain') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'favourite'] = True if request.form.get('favourite') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'garden'] = True if request.form.get('garden') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'history'] = True if request.form.get('history') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'late'] = True if request.form.get('late') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'music'] = True if request.form.get('music') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'pool'] = True if request.form.get('pool') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'quiz'] = True if request.form.get('quiz') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'roast'] = True if request.form.get('roast') == 'on' else False
        df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'sport'] = True if request.form.get('sport') == 'on' else False
        # print(df_reviews.loc[df_reviews['pub_identity'] == pub_id])
        return df_reviews