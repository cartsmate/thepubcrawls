from flask import request
from config import Configurations
from app.models.pub.pub import Pub
from app.models.review.review import Review

config = Configurations().get_config()


class FormNew:

    def get_pub(self, pub_id):
        new_pub = Pub(pub_identity=pub_id, pub_deletion=request.form['pub_deletion'], place=request.form['place'],
                      name=request.form['name'], address=request.form['address'],
                      latitude=request.form['latitude'], longitude=request.form['longitude'],
                      station_identity=request.form['station_identity'],
                      area_identity=request.form['area_identity'], category=request.form['category'].lower())
        return new_pub

    def get_review(self, pub_id):
        if request.form.get('star') is None:
            star = ""
        else:
            star = request.form.get('star').lower()
        if request.form.get('reviewer') is None:
            reviewer = ""
        else:
            reviewer = request.form.get('reviewer').lower()

        new_review = Review(review_identity=request.form['review_identity'], pub_identity=pub_id,
                            review_deletion=request.form['review_deletion'], visit=request.form['visit'], star=star,
                            atmosphere=request.form['atmosphere'], cleanliness=request.form['cleanliness'],
                            clientele=request.form['clientele'], decor=request.form['decor'],
                            entertainment=request.form['entertainment'], food=request.form['food'],
                            friendliness=request.form['friendliness'], opening=request.form['opening'],
                            price=request.form['price'], selection=request.form['selection'], reviewer=reviewer)
        return new_review
