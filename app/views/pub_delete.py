import pandas as pd
from flask import redirect, url_for
from app import app
from config import Configurations
from functions.functions import Functions
from app.static.pythonscripts.dataframes import Dataframes

config = Configurations().get_config()


@app.route("/pub/delete/<pub_id>")
def pub_delete(pub_id):
    print('/pub/delete/<pub_id>')
    df_pubs = Functions().get_pubs()
    df_pubs.loc[df_pubs['pub_identity'] == pub_id, 'pub_deletion'] = True
    Dataframes().to_csv(df_pubs, 'pub')
    s3_resp = Functions().s3_write(df_pubs, config['pub']['aws_key'])

    # s3_resp = Functions().s3_write(df_pubs.to_csv(sep=',', encoding='utf-8', index=False), config['pub']['aws_key'])
    # print(s3_resp)
    df_reviews = Functions().get_reviews()
    df_reviews.loc[df_reviews['pub_identity'] == pub_id, 'review_deletion'] = True
    Dataframes().to_csv(df_reviews, 'review')
    s3_resp = Functions().s3_write(df_reviews, config['review']['aws_key'])

    # s3_resp = Functions().s3_write(df_reviews.to_csv(sep=',', encoding='utf-8', index=False), config['review']['aws_key'])
    # print(s3_resp)
    df_stations = Functions().get_stations()
    df_all = Functions().get_pubs_reviews()
    all_json = Functions().df_to_dict(df_all)
    df_all_trunc = df_all[['name', 'station_identity']]
    df_all_count = df_all_trunc.groupby(['station_identity'], as_index=False).count()
    df_all_latlng = pd.merge(df_all_count, df_stations, how='left', on='station_identity').rename(
        columns={'name': 'count'}).astype(str)
    df_all_latlng['colour'] = config['colour']['primary']
    station_all_json = Functions().df_to_dict(df_all_latlng)
    view = "all"
    return redirect(url_for('map_by_all'))

        # url_for('pub_map', google_key=config['google_key'], full=all_json,
        #             summary=station_all_json, map_view=view, map_lat=51.5, map_lng=-0.1))


        # except Exception as e:
        #     print(e)
        #     return render_template('404.html', error=e)
