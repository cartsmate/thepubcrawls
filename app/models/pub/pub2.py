import json
from app.models.pub.pub_identity import PubIdentity
from app.models.pub.address import Address
from app.models.pub.category import Category
from app.models.pub.pub_deletion import PubDeletion
from app.models.pub.pub_latitude import PubLatitude
from app.models.pub.pub_longitude import PubLongitude
from app.models.pub.pub_name import PubName
from app.models.pub.place import Place
from app.models.pub.rank import Rank
from app.models.pub.colour import Colour
from app.models.pub.detail import Detail
from app.models.pub.pub_base import Base
from app.models.pub.pub_base import NewId
from app.models.area.area import Area
from app.models.station.station import Station
from app.models.review.review2 import Review2
from app.models.area.area_identity import AreaIdentity
from app.models.station.station_identity import StationIdentity


class Pub2:

    # def __init__(self, pub_id):
    #     self.pub_identity = PubIdentity(pub_id)
    #     # self.Foo = Foo()
    #     self.address = Address()
    #     self.area_identity = AreaIdentity()
    #     self.category = Category()
    #     self.place = Place()
    #     self.colour = Colour()
    #     self.pub_deletion = PubDeletion()
    #     self.pub_latitude = PubLatitude()
    #     self.pub_longitude = PubLongitude()
    #     self.pub_name = PubName()
    #     self.rank = Rank()
    #     self.station_identity = StationIdentity()

    def __init__(self, pub_deletion=PubDeletion(), place=Place(), pub_name=PubName(),
                 address=Address(), pub_latitude=PubLatitude(), pub_longitude=PubLongitude(), category=Category(),
                 rank=Rank(), station_identity=StationIdentity(), area_identity=AreaIdentity(), pub_identity=PubIdentity(),
                 colour=Colour(), detail=Detail()):
        self.pub_identity = pub_identity
        self.address = address
        self.area_identity = area_identity
        self.category = category
        self.place = place
        self.colour = colour
        self.pub_deletion = pub_deletion

        self.pub_latitude = pub_latitude
        self.pub_longitude = pub_longitude
        self.pub_name = pub_name
        self.rank = rank
        self.station_identity = station_identity
        self.detail = detail
        # self.newid = newid
        # self.base = base

    # def attributes(self, pub_deletion=None, place=None, pub_name=PubName(), address=Address(),
    #              pub_latitude=PubLatitude(), pub_longitude=PubLongitude(), category=Category(), rank=Rank(),
    #              station_identity=StationIdentity(), area_identity=AreaIdentity(), pub_identity=PubIdentity(),
    #              colour=Colour(), base=Base()):
    #     if pub_deletion is None:
    #         pub_deletion = self.pub_deletion



    def reprJSON(self):
        return dict(pub_identity=self.pub_identity, pub_deletion=self.pub_deletion, area_identity=self.area_identity,
                    station_identity=self.station_identity, address=self.address, category=self.category,
                    latitude=self.pub_latitude, longitude=self.pub_longitude, name=self.pub_name, place=self.place,
                    rank=self.rank)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)
