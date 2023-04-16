import os
import pandas as pd
from flask import render_template, request, redirect, url_for, g, session
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
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    print('pub_read')
    df_pub_review = Functions().get_pub_review(pub_id)
    print(df_pub_review)
    if request.method == 'GET':
        print('pub_read: GET')
        return render_template("pub_read.html", form_type='read', google_key=config2['google_key'],
                               pub_review=Functions().df_to_dict(df_pub_review), config=config)

    if request.method == 'POST':
        print('pub_read: POST')
        if df_pub_review.empty:
            print('new pub')
            if df_pub_review.loc[df_pub_review['place'] == str(request.form['place'])].empty:
                print('new / not dupe pub')
                df_new_pub = FormNew().get_pub(pub_id)

                df_pub_appended = Dataframes().append_df(Functions().get_pubs(), df_new_pub)
                if df_pub_appended.shape[1] == len(config['pub']['model']):
                    Dataframes().to_csv(df_pub_appended, 'pub')
                    s3_resp = Functions().s3_write(df_pub_appended, config['pub']['aws_key'])
                else:
                    print('Error in processing')

                df_new_review = FormNew().get_review(pub_id)
                print(df_new_review)
                df_review_appended = Dataframes().append_df(Functions().get_reviews(), df_new_review)
                print(df_review_appended)
                if df_review_appended.shape[1] == len(config['review']['model']):
                    Dataframes().to_csv(df_review_appended, 'review')
                    s3_resp = Functions().s3_write(df_review_appended, config['review']['aws_key'])
                else:
                    print('Error in processing')
                df_new_merged = Dataframes().merge_dfs(df_new_pub, df_new_review)
                return render_template('pub_read.html', form_type='read', google_key=config2['google_key'],
                                       pub_review=Functions().df_to_dict(df_new_merged), config=config)
            else:
                print('duplicate pub')
                df_pubs_reviews = Functions().get_pubs_reviews()
                dupe_id = df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])]['pub_identity']
                return render_template("pop_up_dupe.html",
                                       pub_review=Functions().df_to_dict(
                                           df_pubs_reviews.loc[df_pubs_reviews['place'] == str(request.form['place'])]),
                                       dupe_id=dupe_id)
        else:
            print('edit pub')
            df_pubs_updated = FormInput().get_pub(Functions().get_pubs(), pub_id)
            Dataframes().to_csv(df_pubs_updated, 'pub')
            s3_resp = Functions().s3_write(df_pubs_updated, config['pub']['aws_key'])

            df_review_updated = FormInput().get_review(Functions().get_reviews(), pub_id)
            Dataframes().to_csv(df_review_updated, 'review')
            s3_resp = Functions().s3_write(df_review_updated, config['review']['aws_key'])

            df_pub_review = Functions().get_pub_review(pub_id)
            pub_review_json = Functions().df_to_dict(df_pub_review)
            print(df_pub_review)
            return render_template('pub_read.html', form_type='read', google_key=config2['google_key'],
                                   pub_review=pub_review_json, config=config)
