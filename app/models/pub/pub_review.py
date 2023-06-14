from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2


class PubReview2(Pub2, Review2):

    def __init__(self, pub_d, pub_p):
        self.pub_deletion = pub_d
        self.place = pub_p
