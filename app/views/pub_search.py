import json
import numpy as np
from flask import render_template, redirect, url_for, g, session, request
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/pub/search/")
def pub_search():
    print('pub_search')
    # pet = request.args.get('pet')

    pet = request.args.get('pet')
    if pet.title() == 'True':
        pet_list = ['True']
    else:
        pet_list = ['True', 'False']

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

    quiz = request.args.get('quiz')
    if quiz.title() == 'True':
        quiz_list = ['True']
    else:
        quiz_list = ['True', 'False']

    pool = request.args.get('pool')
    if pool.title() == 'True':
        pool_list = ['True']
    else:
        pool_list = ['True', 'False']

    lively = request.args.get('lively')
    if lively.title() == 'True':
        lively_list = ['True']
    else:
        lively_list = ['True', 'False']

    df_scores = Functions().get_pubs_reviews()

    filtered_values = df_scores.loc[(
        df_scores['pet'].astype(str).isin(pet_list) &
        df_scores['tv'].astype(str).isin(tv_list) &
        df_scores['garden'].astype(str).isin(garden_list) &
        df_scores['music'].astype(str).isin(music_list) &
        df_scores['late'].astype(str).isin(late_list) &
        df_scores['meals'].astype(str).isin(meals_list) &
        df_scores['toilets'].astype(str).isin(toilets_list) &
        df_scores['cheap'].astype(str).isin(cheap_list) &
        df_scores['games'].astype(str).isin(games_list) &
        df_scores['quiz'].astype(str).isin(quiz_list) &
        df_scores['pool'].astype(str).isin(pool_list) &
        df_scores['lively'].astype(str).isin(lively_list)
    )]
    print(filtered_values[['pet', 'tv', 'garden', 'music', 'late', 'meals', 'toilets', 'cheap', 'games', 'quiz', 'pool', 'lively']])
    pubs_reviews_json = Functions().df_to_dict(filtered_values)
    # ?tv = false & garden = false & music = false & late = false & meals = false & toilets = false & cheap = false & games = false
    return render_template('pub_search.html', config=config, pubs_reviews=pubs_reviews_json, pet=pet, tv=tv,
                           garden=garden, music=music, late=late, meals=meals, toilets=toilets, cheap=cheap,
                           games=games, quiz=quiz, pool=pool, lively=lively, config2=config2)
