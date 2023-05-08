from datetime import date
from functions.functions import Functions
from ..models.pub_identity import PubIdentity


class Review:
    def __init__(self, review_identity, review_deletion, pub_identity,
                 visit, star, reviewer, rating,
                 atmosphere, cleanliness,
                 clientele, decor, entertainment, food, friendliness, opening, price, selection,
                 tv, garden, music, late, meals, toilets, cheap, games, pet, quiz):
        self.pub_identity = pub_identity
        self.review_identity = review_identity
        self.review_deletion = review_deletion
        self.visit = visit
        self.star = star
        self.atmosphere = atmosphere
        self.cleanliness = cleanliness
        self.clientele = clientele
        self.decor = decor
        self.entertainment = entertainment
        self.food = food
        self.friendliness = friendliness
        self.opening = opening
        self.price = price
        self.selection = selection
        self.reviewer = reviewer
        self.rating = rating
        self.tv = tv
        self.garden = garden
        self.music = music
        self.late = late
        self.meals = meals
        self.toilets = toilets
        self.cheap = cheap
        self.games = games
        self.pet = pet
        self.quiz = quiz
