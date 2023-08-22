import os
import json
import pandas as pd
import uuid
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

        form_visible_list = []
        table_visible_list = []
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
        pub_id = uuid.uuid4()
        class_list = [Pub2(), Review2(), Area(), Station()]
        # class_list = [Review2(), Area(), Station()]
        for cl in class_list:
            for k, v in cl.__dict__.items():
                fields_list.append(v.name)
                if v.form_visible == 'true':
                    form_visible_list.append(v.name)
                if v.table_visible == 'true':
                    table_visible_list.append(v.name)
                if v.required == 'true':
                    required_list.append(v.name)
                try:
                    if v.icon is not 'none':
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
        # print('form_visible_list')
        # print(form_visible_list)
        selected_pub_colour = '#0275d8'
        other_pub_colour = '#d9534f'
        # print('icon_list')
        # print(icon_list)
        return dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
               required_list, form_visible_list, table_visible_list, icon_list, fields_list, ignore_list, \
               selected_pub_colour, other_pub_colour
