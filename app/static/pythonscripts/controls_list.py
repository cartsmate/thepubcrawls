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
        ignore_list = ['review_deletion', 'review_identity', 'pub_identity', 'detail']

        visible_list = []
        required_list = []
        alias_list = []
        icon_list = []
        dropdown_list = []
        input_list = []
        star_list = []
        date_list = []
        slider_list = []
        check_list = []
        fields_list = []
        class_list = [Pub2(), Review2(), Area(), Station()]
        for cl in class_list:
            for k, v in cl.__dict__.items():
                fields_list.append(v.name)
                if v.visible == True:
                    visible_list.append(v.name)
                if v.required == True:
                    required_list.append(v.name)
                try:
                    if v.icon is not None:
                        icon_list.append(v.name)
                except:
                    pass
                try:
                    if v.alias1:
                        alias_json = {v.name: v.alias1 + " " + v.alias2}
                        alias_list.append(alias_json)
                    else:
                        alias_json = {v.name: v.alias}
                        alias_list.append(alias_json)
                except:
                    pass
                if v.control == "dropdown":
                    dropdown_list.append(v.name)
                if v.control == "star":
                    star_list.append(v.name)
                if v.control == "input":
                    input_list.append(v.name)
                if v.control == "date":
                    date_list.append(v.name)
                if v.control == "slider":
                    slider_list.append(v.name)
                if v.control == "check":
                    check_list.append(v.name)

        return dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
               required_list, visible_list, icon_list, fields_list, ignore_list
