import os
import pandas as pd
from flask import render_template, request
from app import app
from config import Configurations
from functions.functions import Functions
from functions.form_input import FormInput
from app.static.pythonscripts.form_new import FormNew
from app.static.pythonscripts.dataframes import Dataframes

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/<pub_id>", methods=['GET', 'POST'])
def pub_read(pub_id):
    df_pub_review = Functions().get_pub_review(pub_id)
    if request.method == 'GET':
        return render_template("pub_read.html", form_type='read', google_key=config2['google_key'],
                               pub_review=Functions().df_to_dict(df_pub_review), config=config)

    if request.method == 'POST':
        if df_pub_review.empty:
            if df_pub_review.loc[df_pub_review['place'] == str(request.form['place'])].empty:
                Dataframes().merge_to_csv(Functions().get_pubs(), FormNew().get_pub(pub_id), 'pub')
                # s3_resp = Functions().s3_write(os.getcwd() + '/files/' + config['pub']['aws_key'], config['pub']['aws_key'])

                Dataframes().merge_to_csv(Functions().get_reviews(), FormNew().get_review(pub_id), 'pub')
                # s3_resp = Functions().s3_write(os.getcwd() + '/files/' + config['review']['aws_key'], config['review']['aws_key'])
                return render_template('pub_read.html', form='read', google_key=config2['google_key'],
                                       pub_review=Functions().df_to_dict(df_pub_review), config=config)
            else:
                df_pubs_reviews = Functions().get_pubs_reviews()
                dupe_id = df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])]['pub_identity']
                return render_template("pop_up_dupe.html",
                                       pub_review=Functions().df_to_dict(
                                           df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])]),
                                       dupe_id=dupe_id)
        else:
            df_pubs_updated = FormInput().get_pub(Functions().get_pubs(), pub_id)
            Dataframes().to_csv(df_pubs_updated, 'pub')
            # _path = os.getcwd() + '/files/venues.csv'
            # print(_path)
            s3_resp = Functions().s3_write(df_pubs_updated, config['pub']['aws_key'])

            df_review_updated = FormInput().get_review(Functions().get_reviews(), pub_id)
            Dataframes().to_csv(df_review_updated, 'review')
            s3_resp = Functions().s3_write(df_review_updated, config['review']['aws_key'])

            df_pub_review = Functions().get_pub_review(pub_id)
            pub_review_json = Functions().df_to_dict(df_pub_review)

            return render_template('pub_read.html', form_type='read', google_key=config2['google_key'],
                                   pub_review=pub_review_json, config=config)
