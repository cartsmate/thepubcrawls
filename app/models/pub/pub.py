from app.static.pythonscripts.uuid import Uuid

class Pub():
    def __init__(self, pub_identity=0, pub_deletion=False, place="", name="", address="", latitude=0, longitude=0, category="", rank=0,
                 station_identity=0, area_identity=0):
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
