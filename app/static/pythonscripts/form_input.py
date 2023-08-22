from flask import request
from config import Configurations
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.diary.week import Week
from app.static.pythonscripts.controls_list import ControlsList
config = Configurations().get_config()


class FormInput:

    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
        required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
        ignore_list, selected_pub_colour, other_pub_colour = ControlsList().get_control_lists()

    def get_pub(self, df_pubs, pub_id):
        for pub in list(Pub2().__dict__.keys()):
            print(pub + ' : ' + request.form[pub])
            df_pubs.loc[df_pubs['pub_identity'] == pub_id, pub] = request.form[pub]
        return df_pubs

    def get_review(self, df_reviews, pub_id):
        # print(df_reviews.loc[df_reviews['quiz'] == pub_id])

        for review in list(Review2().__dict__.keys()):
            if review in self.icon_list:
            # if review not in self.ignore_list:
                print(review + ' : ' + str(request.form.get(review)))
                df_reviews.loc[df_reviews['pub_identity'] == pub_id, review] = 'true' \
                    if request.form.get(review) == 'on' \
                    else 'false'
            else:
                print(review + ' : ' + str(request.form.get(review)))
                df_reviews.loc[df_reviews['pub_identity'] == pub_id, review] = request.form[review]
            # if review == 'detail':
            #     print(review + ' : ' + request.form[review])
            #     df_reviews.loc[df_reviews['pub_identity'] == pub_id, review] = request.form[review]
            # print(df_reviews.loc[df_reviews['quiz'] == pub_id])
        print('df_reviews')
        print(df_reviews.loc[df_reviews['pub_identity'] == pub_id])
        return df_reviews

    def get_diary(self, df_diary, pub_id):
        for diary in list(Week().__dict__.keys()):
            df_diary.loc[df_diary['pub_identity'] == pub_id, diary] = request.form[diary]
            print(diary + ' : ' + request.form[diary])
        return df_diary
