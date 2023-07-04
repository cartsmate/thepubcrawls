from app.models.station.station_deletion import StationDeletion
from app.models.station.station_identity import StationIdentity
from app.models.station.station_name import StationName
from app.models.station.station_latitude import StationLatitude
from app.models.station.station_longitude import StationLongitude
from app.models.station.zone import Zone
from app.models.station.postcode import Postcode
from app.models.direction.direction_identity import DirectionIdentity


class Station:
    def __init__(self, station_deletion=StationDeletion(), station_name=StationName(),
                 station_latitude=StationLatitude(), station_longitude=StationLongitude(), zone=Zone(),
                 postcode=Postcode(), direction_identity=DirectionIdentity(), station_identity=StationIdentity()):
        self.station_identity = station_identity
        self.station_deletion = station_deletion
        self.station_name = station_name
        self.station_latitude = station_latitude
        self.station_longitude = station_longitude
        self.zone = zone
        self.postcode = postcode
        self.direction_identity = direction_identity
