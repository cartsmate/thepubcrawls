import pandas as pd
from flask import redirect, url_for
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()


@app.route("/pub/delete/<pub_id>")
def pub_delete(pub_id):
    print('/pub/delete/<pub_id>')
    df_pubs = function.get_pubs()
    df_reviews = function.get_reviews()
    df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'pub_deletion'] = True
    s3_resp = function.write_csv_to_s3(df_pubs.to_csv(sep=',', encoding='utf-8', index=False), config['aws_key_pub'])
    # print(s3_resp)
    df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'review_deletion'] = True
    s3_resp = function.write_csv_to_s3(df_reviews.to_csv(sep=',', encoding='utf-8', index=False),
                                       config['aws_key_review'])
    # print(s3_resp)
    df_stations = function.get_stations()
    df_all = function.get_pubs_reviews()
    all_json = function.df_to_dict(df_all)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity').rename(
        columns={'name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour_primary']
    station_all_json = function.df_to_dict(df_all_latlng)
    view = "all"
    return redirect(url_for('map_by_all'))

        # url_for('pub_map', google_key=config['google_key'], full=all_json,
        #             summary=station_all_json, map_view=view, map_lat=51.5, map_lng=-0.1))


        # except Exception as e:
        #     print(e)
        #     return render_template('404.html', error=e)
