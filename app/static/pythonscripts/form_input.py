from flask import request
from config import Configurations
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.static.pythonscripts.controls_list import ControlsList
config = Configurations().get_config()


class FormInput:

    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
        required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
        ignore_list = ControlsList().get_control_lists()

    def get_pub(self, df_pubs, pub_id):
        for pub in list(Pub2().__dict__.keys()):
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, pub] = request.form[pub]
            print(pub + ' : ' + request.form[pub])
        # print('new pub from input: df_pubs:')
        # print(df_pubs[['pub_identity', 'pub_name', 'pub_deletion']])
        return df_pubs

    def get_review(self, df_reviews, pub_id):
        for review in list(Review2().__dict__.keys()):
            if review not in self.ignore_list:
                print(review + ' : ' + str(request.form.get(review)))
                df_reviews.loc[df_reviews['pub_identity'] == pub_id, review] = True if request.form.get(review) == 'on' else False
            if review == 'detail':
                print(review + ' : ' + request.form[review])
                df_reviews.loc[df_reviews['pub_identity'] == pub_id, review] = request.form[review]
        return df_reviews