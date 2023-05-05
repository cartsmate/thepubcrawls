import json
import numpy as np
from flask import render_template, redirect, url_for, g, session, request
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()


@app.route("/pub/search/")
def pub_search():
    print('pub_search')
    # pet = request.args.get('pet')

    tv = request.args.get('tv')
    if tv.title() == 'True':
        tv_list = ['True']
    else:
        tv_list = ['True', 'False']

    garden = request.args.get('garden')
    if garden.title() == 'True':
        garden_list = ['True']
    else:
        garden_list = ['True', 'False']

    music = request.args.get('music')
    if music.title() == 'True':
        music_list = ['True']
    else:
        music_list = ['True', 'False']

    late = request.args.get('late')
    if late.title() == 'True':
        late_list = ['True']
    else:
        late_list = ['True', 'False']

    meals = request.args.get('meals')
    if meals.title() == 'True':
        meals_list = ['True']
    else:
        meals_list = ['True', 'False']

    toilets = request.args.get('toilets')
    if toilets.title() == 'True':
        toilets_list = ['True']
    else:
        toilets_list = ['True', 'False']

    cheap = request.args.get('cheap')
    if cheap.title() == 'True':
        cheap_list = ['True']
    else:
        cheap_list = ['True', 'False']

    games = request.args.get('games')
    if games.title() == 'True':
        games_list = ['True']
    else:
        games_list = ['True', 'False']

    df_scores = Functions().get_pubs_reviews()

    filtered_values = df_scores.loc[(
        df_scores['tv'].astype(str).isin(tv_list) &
        df_scores['garden'].astype(str).isin(garden_list) &
        df_scores['music'].astype(str).isin(music_list) &
        df_scores['late'].astype(str).isin(late_list) &
        df_scores['meals'].astype(str).isin(meals_list) &
        df_scores['toilets'].astype(str).isin(toilets_list) &
        df_scores['cheap'].astype(str).isin(cheap_list) &
        df_scores['games'].astype(str).isin(games_list)
    )]
    print(filtered_values[['name', 'tv', 'garden', 'meals', 'toilets', 'cheap', 'games']])
    pubs_reviews_json = Functions().df_to_dict(filtered_values)
    # ?tv = false & garden = false & music = false & late = false & meals = false & toilets = false & cheap = false & games = false
    return render_template('pub_search.html', config=config, pubs_reviews=pubs_reviews_json, tv=tv, garden=garden,
                           music=music, late=late, meals=meals, toilets=toilets, cheap=cheap, games=games)
