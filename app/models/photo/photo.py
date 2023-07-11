from app.models.photo.photo_deletion import PhotoDeletion
from app.models.photo.photo_identity import PhotoIdentity
from app.models.pub.pub_identity import PubIdentity


class Photo:

    # def __init__(self, pub_id):
    #     self.photo_identity = PhotoIdentity()
    #     self.photo_deletion = PhotoDeletion()
    #     self.pub_identity = PubIdentity(pub_id)

    def __init__(self, photo_identity=PhotoDeletion(), photo_deletion=PhotoDeletion(), pub_identity=PubIdentity()):
        self.photo_identity = photo_identity
        self.photo_deletion = photo_deletion
        self.pub_identity = pub_identity
