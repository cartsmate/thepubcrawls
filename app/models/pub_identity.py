from functions.functions import Functions


class PubIdentity:
    def __init__(self, pub_identity=str(Functions().generate_uuid())):
        self.pub_identity = pub_identity
