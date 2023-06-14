import os
import json
import pandas as pd
from config import Configurations
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.area.area import Area
from app.models.photo.photo import Photo
from app.models.station.station import Station

config = Configurations().get_config()


class ControlsList:

    def get_control_lists(self):
        new_pub2 = Pub2()
        pub = []
        for v in new_pub2.__dict__.values():
            pub.append(v.__dict__)
        pub_dict = {"pub": pub}
        pub_json = json.dumps(pub_dict)
        # print(pub_json)

        new_review2 = Review2()
        review = []
        for v in new_review2.__dict__.values():
            review.append(v.__dict__)
        review_dict = {"review": review}
        review_json = json.dumps(review_dict)
        # print(review_json)

        new_area = Area()
        new_photo = Photo()

        new_photo_col = [
            new_photo.pub_identity.name,
            new_photo.photo_deletion.name,
            new_photo.photo_identity.name
        ]
        new_photo_val = [
            new_photo.pub_identity.value,
            new_photo.photo_deletion.value,
            new_photo.photo_identity.value
        ]
        df_new_photo = pd.DataFrame(columns=new_photo_col, data=[new_photo_val])
        new_area_col = [
            new_area.area_name.name,
            new_area.area_identity.name,
            new_area.area_deletion.name,
            new_area.photo_identity.name,
            new_area.area_type.name,
            new_area.area_longitude.name,
            new_area.area_latitude.name
        ]
        new_area_val = [
            new_area.area_name.value,
            new_area.area_identity.value,
            new_area.area_deletion.value,
            new_area.photo_identity.value,
            new_area.area_type.value,
            new_area.area_longitude.value,
            new_area.area_latitude.value
        ]
        df_new_area = pd.DataFrame(columns=new_area_col, data=[new_area_val])
        new_station = Station()
        new_station_col = [
            new_station.station_name.name,
            new_station.station_identity.name,
            new_station.station_deletion.name,
            new_station.station_latitude.name,
            new_station.station_longitude.name,
            new_station.postcode.name,
            new_station.zone.name
        ]
        new_station_val = [
            new_station.station_name.value,
            new_station.station_identity.value,
            new_station.station_deletion.value,
            new_station.station_latitude.value,
            new_station.station_longitude.value,
            new_station.postcode.value,
            new_station.zone.value
        ]
        df_new_station = pd.DataFrame(columns=new_station_col, data=[new_station_val])

        new_pub_col = [
            new_pub2.address.name,
            new_pub2.area_identity.name,
            new_pub2.category.name,
            new_pub2.pub_latitude.name,
            new_pub2.pub_longitude.name,
            new_pub2.pub_name.name,
            new_pub2.place.name,
            new_pub2.pub_deletion.name,
            new_pub2.pub_identity.name,
            new_pub2.rank.name,
            new_pub2.station_identity.name]

        new_pub_val = [
            new_pub2.address.value,
            new_pub2.area_identity.value,
            new_pub2.category.value,
            new_pub2.pub_latitude.value,
            new_pub2.pub_longitude.value,
            new_pub2.pub_name.value,
            new_pub2.place.value,
            new_pub2.pub_deletion.value,
            new_pub2.pub_identity.value,
            new_pub2.rank.value,
            new_pub2.station_identity.value]

        df_new_pub = pd.DataFrame(columns=new_pub_col, data=[new_pub_val])

        new_review_col = [
            new_pub2.pub_identity.name,
            new_review2.review_identity.name,
            new_review2.review_deletion.name,
            new_review2.brunch.name,
            new_review2.dart.name,
            new_review2.entertain.name,
            new_review2.favourite.name,
            new_review2.garden.name,
            new_review2.history.name,
            new_review2.late.name,
            new_review2.music.name,
            new_review2.pool.name,
            new_review2.quiz.name,
            new_review2.roast.name,
            new_review2.sport.name]

        new_review_val = [
            new_pub2.pub_identity.value,
            new_review2.review_identity.value,
            new_review2.review_deletion.value,
            new_review2.brunch.value,
            new_review2.dart.value,
            new_review2.entertain.value,
            new_review2.favourite.value,
            new_review2.garden.value,
            new_review2.history.value,
            new_review2.late.value,
            new_review2.music.value,
            new_review2.pool.value,
            new_review2.quiz.value,
            new_review2.roast.value,
            new_review2.sport.value]
        # print(new_review_val)

        df_new_review = pd.DataFrame(columns=new_review_col, data=[new_review_val])

        df_new_pub = pd.DataFrame(columns=new_pub_col, data=[new_pub_val])

        df_pub_area = pd.merge(df_new_pub, df_new_area, how="left", on=new_pub2.area_identity.name)
        df_pub_area_station = pd.merge(df_pub_area, df_new_station, how="left", on=new_pub2.station_identity.name)
        df_pub_area_station_photo = pd.merge(df_pub_area_station, df_new_photo, how="left",
                                             on=new_pub2.pub_identity.name)
        pub_fields = list(df_pub_area_station_photo)

        df_new_review = pd.DataFrame(columns=new_review_col, data=[new_review_val])
        review_fields = list(df_new_review)

        control_list = []
        alias_list = []
        pub2_required_list = []
        pub2_visible_list = []
        icon_list = []
        review2_required_list = []
        review2_visible_list = []
        for pub in pub_dict["pub"]:
            control_list.append({pub["name"]: pub["control"]})
            alias_list.append({pub["name"]: pub["alias"]})
            if pub["required"] == True:
                pub2_required_list.append(pub["name"])
            if pub["visible"] == True:
                pub2_visible_list.append(pub["name"])
        for review in review_dict["review"]:
            # print(review["name"])
            control_list.append({review["name"]: review["control"]})
            try:
                alias_list.append({review["name"]: review["alias1"] + " " + review["alias2"]})
            except:
                alias_list.append({review["name"]: review["alias"]})
            icon_list.append({review["name"]: review["icon"]})
            review2_required_list.append({review["name"]: review["required"]})
            review2_visible_list.append({review["name"]: review["visible"]})

        dropdown_list = []
        input_list = []
        star_list = []
        date_list = []
        slider_list = []
        check_list = []

        for x in control_list:
            # print(list(x.keys()))
            # print(list(x.values()))
            if "dropdown" in list(x.values()):
                dropdown_list.append(list(x.keys())[0])
            if "star" in list(x.values()):
                star_list.append(list(x.keys())[0])
            if "input" in list(x.values()):
                input_list.append(list(x.keys())[0])
            if "date" in list(x.values()):
                date_list.append(list(x.keys())[0])
            if "slider" in list(x.values()):
                slider_list.append(list(x.keys())[0])
            if "check" in list(x.values()):
                check_list.append(list(x.keys())[0])

        return dropdown_list, star_list, input_list, date_list, slider_list, check_list, control_list, alias_list, \
               pub2_required_list, pub2_visible_list, icon_list, review2_required_list, review2_visible_list, \
               pub_fields, review_fields
