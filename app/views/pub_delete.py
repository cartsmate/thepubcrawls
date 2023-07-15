import pandas as pd
from flask import redirect, url_for
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.csv import Csv
from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.static.pythonscripts.entities_single import EntitiesSingle

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/delete/<pub_id>")
def pub_delete(pub_id):
    print('/pub/delete/<pub_id>')
    # pubs_area = EntitiesMulti().get_pubs_area()
    # id_type = pubs_area.loc[pubs_area['pub_identity'] == pub_id, 'area_name'].iloc[0]
    df_pubs = Csv().get_pubs()
    # df_pubs = S3().get_s3_pubs()
    df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'pub_deletion'] = True
    Dataframes().to_csv(df_pubs, 'pub')
    # s3_resp = S3().s3_write(df_pubs, config['pub']['aws_key'])

    # s3_resp = Functions().s3_write(df_pubs.to_csv(sep=',', encoding='utf-8', index=False), config['pub']['aws_key'])
    # print(s3_resp)
    df_reviews = Csv().get_reviews()
    # df_reviews = S3().get_s3_reviews()
    df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'review_deletion'] = True
    Dataframes().to_csv(df_reviews, 'review')
    # s3_resp = S3().s3_write(df_reviews, config['review']['aws_key'])
    station_id = df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'station_identity'].values[0]
    print(station_id)
    # dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    # required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    # ignore_list = ControlsList().get_control_lists()

    # df_pubs_reviews = EntitiesMulti().get_pubs_reviews_stations()

    # s3_resp = Functions().s3_write(df_reviews.to_csv(sep=',', encoding='utf-8', index=False), config['review']['aws_key'])
    # print(s3_resp)
    # df_stations = Csv().get_stations()
    # stations_json = Dataframes().df_to_dict(df_stations)
    # df_areas = Csv().get_areas()
    # areas_json = Dataframes().df_to_dict(df_areas)
    # # df_stations = S3().get_s3_stations()
    # df_all = EntitiesMulti().get_pubs_reviews()
    # all_json = Dataframes().df_to_dict(df_all)
    # df_all_trunc = df_all[['pub_name', 'station_identity']]
    # df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    # df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity').rename(
    #     columns={'pub_name': 'count'}).astype(str)
    # # df_all_latlng['colour'] = config['colour']['primary']
    # station_all_json = Dataframes().df_to_dict(df_all_latlng)
    # view = "all"

    # df_selection = df_pubs_reviews.loc[df_pubs_reviews['station_identity'] == station]

    # heading = df_selection.iloc[0]['station_name'] + " Pubs"

    # return redirect(url_for('pub_list/area/'))
    # url_base = "http://127.0.0.1:5000"
    # url = url_base + "/pub/list/?direction=all&station=" + station_id + \
    #       "&zoom=16&brunch=false&dart=false&entertain=false&favourite=false&garden=false&history=false&late=false&music=false&pool=false&quiz=false&roast=false&sport=false"

    return redirect(url_for('pub_list', direction='all', station=station_id, zoom=16))
                    # ,
                            # form_type='list',
                            # filter=heading,
                            # review_obj=Review2(pub_id), form_obj=form_obj,
                            # pubs_reviews=pubs_reviews_json, pubs_selection=pubs_selection_json,
                            # map_lat=review_lat, map_lng=review_long, config2=config2, map_zoom=zoom,
                            # google_key=config2['google_key'],
                            # visible=visible, alias=alias, headers=headers, icon_list=icon_list,
                            # areas=areas_json, stations=stations_json,
                            # station=station, direction=direction, total_rows=total_rows
                    # ))

                            # list_type='area_name', id_type=id_type))

        # url_for('pub_map', google_key=config['google_key'], full=all_json,
        #             summary=station_all_json, map_view=view, map_lat=51.5, map_lng=-0.1))


        # except Exception as e:
        #     print(e)
        #     return render_template('404.html', error=e)
