from app.models.review.brunch import Brunch
from app.models.review.dart import Dart
from app.models.review.garden import Garden
from app.models.review.favourite import Favourite
from app.models.review.history import History
from app.models.review.late import Late
from app.models.review.music import Music
from app.models.review.entertain import Entertain
from app.models.review.pool import Pool
from app.models.review.quiz import Quiz
from app.models.review.review_deletion import ReviewDeletion
from app.models.review.roast import Roast
from app.models.review.sport import Sport
from app.models.review.review_identity import ReviewIdentity
from app.models.pub.pub_identity import PubIdentity


class Review2():
    # def __init__(self, pub_id):
    #     self.brunch = Brunch()
    #     self.dart = Dart()
    #     self.detail = Detail()
    #     self.entertain = Entertain()
    #     self.favourite = Favourite()
    #     self.garden = Garden()
    #     self.history = History()
    #     self.late = Late()
    #     self.music = Music()
    #     self.pool = Pool()
    #     self.pub_identity = PubIdentity(pub_id)
    #     self.quiz = Quiz()
    #     self.review_deletion = ReviewDeletion()
    #     self.review_identity = ReviewIdentity()
    #     self.roast = Roast()
    #     self.sport = Sport()

    def __init__(self, review_deletion=ReviewDeletion(), sport=Sport(), garden=Garden(), music=Music(), roast=Roast(),
                 brunch=Brunch(), late=Late(), quiz=Quiz(), pool=Pool(), dart=Dart(), entertain=Entertain(),
                 history=History(), favourite=Favourite(), pub_identity=PubIdentity(),
                 review_identity=ReviewIdentity()):
                 # pub_identity=PubIdentity,
        self.brunch = brunch
        self.dart = dart
        self.entertain = entertain
        self.favourite = favourite
        self.garden = garden
        self.history = history
        self.late = late
        self.music = music
        self.pool = pool
        self.pub_identity = pub_identity
        self.quiz = quiz
        self.review_deletion = review_deletion
        self.review_identity = review_identity
        self.roast = roast
        self.sport = sport
