from functions.functions import Functions


class Pub_Review:
    def __init__(self, pub_identity=str(Functions().generate_uuid()), pub_deletion=False, place="", name="", address="",
                 latitude=51.5, longitude=-0.1, station_identity="", area_identity="", category="", rank=0):
        self.pub_identity = pub_identity
        self.pub_deletion = pub_deletion
        self.place = place
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.category = category
        self.rank = rank
        self.station_identity = station_identity
        self.area_identity = area_identity
