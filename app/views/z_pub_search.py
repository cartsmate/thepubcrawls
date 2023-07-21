import json
from flask import render_template, request
from app import app
from config import Configurations
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.controls_list import ControlsList
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2

config = Configurations().get_config()
config2 = Configurations().get_config2()


# @app.route("/pub/search/<id_area>/")
# def pub_search(id_area):
@app.route("/pub/search/")
def pub_search():
    print('pub_search')

    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    ignore_list, selected_pub_colour, other_pub_colour = ControlsList().get_control_lists()

    # print(id_area)

    review_list = {}
    form_obj = {}
    for review in list(Review2().__dict__.keys()):
        if review not in ignore_list:
            form_obj[review] = request.args.get(review)
            if request.args.get(review) == 'true':
                review_list[review] = ['True']
            else:
                review_list[review] = ['True', 'False']

    filtered_values = EntitiesMulti().get_pubs_reviews()

    for review in review_list:
        filtered_values = filtered_values.loc[(filtered_values[review].astype(str).isin(review_list[review]))]

    # if request.args.get('area') != "":
    #     filtered_values = filtered_values.loc[filtered_values['area_name'] == request.args.get('area')]

    headers = list(filtered_values.columns)
    print('headers')
    print(headers)
    pubs_reviews_json = Dataframes().df_to_dict(filtered_values)

    l3 = [x for x in list(Review2().__dict__.keys()) if x not in ignore_list]

    review_obj_list = []
    for x in Review2().__dict__.values():
        review_obj_list.append(x)

    key_list = list(Review2().__dict__.keys())
    review_object = Review2().__dict__

    inst_pub = Pub2()
    inst_review = Review2()
    inst_pub.__dict__.update(inst_review.__dict__)
    inst_pub_review = inst_pub
    visible = {}
    for k, v in inst_pub_review.__dict__.items():
        visible[k] = v.table_visible
        # print(k)
        # print(v.visible)

    return render_template('pub_search.html', config=config, pubs_reviews=pubs_reviews_json, form_obj=form_obj,
                           config2=config2, review_list=review_list, review_obj=Review2(), ignore_list=ignore_list,
                           features=l3, review_dict=Review2().__dict__.values(), review_obj_list=review_obj_list,
                           key_list=key_list, review_object=review_object, headers=headers, visible=visible,
                           fields_list=fields_list, form_type='search',
                           star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                           check_list=check_list, slider_list=slider_list, date_list=date_list,
                           form_visible_list=form_visible_list, table_visible_list=table_visible_list,
                           required_list=required_list,
                           alias_list=alias_list, icon_list=icon_list)
