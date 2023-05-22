from ..models.pub_identity import PubIdentity


class Photo:
    def __init__(self, pub_identity, photo_identity, photo_deletion):
        self.pub_identity = pub_identity
        self.photo_identity = photo_identity
        self.photo_deletion = photo_deletion
