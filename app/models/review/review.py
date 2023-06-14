from app.models.attribute import Attribute


class Review:

    def __init__(self, review_identity, review_deletion, pub_identity,
                 # visit, star, atmosphere, cleanliness, clientele, decor, entertainment, food, friendliness, opening,
                 # price, selection, rating, reviewer,
                 sport, garden, music, late, roast, brunch, dart, quiz, pool, entertain, history, favourite):
        self.pub_identity = pub_identity
        self.review_deletion = review_deletion
        self.review_identity = review_identity
        # self.visit = visit
        # self.star = star
        # self.atmosphere = atmosphere
        # self.cleanliness = cleanliness
        # self.clientele = clientele
        # self.decor = decor
        # self.entertainment = entertainment
        # self.food = food
        # self.friendliness = friendliness
        # self.opening = opening
        # self.price = price
        # self.selection = selection
        # self.rating = rating
        # self.reviewer = reviewer

        self.sport = sport
        self.garden = garden
        self.music = music
        self.roast = roast
        self.brunch = brunch
        self.late = late

        self.quiz = quiz
        self.pool = pool
        self.dart = dart
        self.entertain = entertain
        self.history = history
        self.favourite = favourite
