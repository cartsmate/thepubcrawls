from app.models.area.area_name import AreaName
from app.models.area.area_deletion import AreaDeletion
from app.models.area.area_identity import AreaIdentity
from app.models.area.area_type import AreaType
from app.models.area.area_latitude import AreaLatitude
from app.models.area.area_longitude import AreaLongitude
from app.models.area.parent_identity import ParentIdentity
from app.models.photo.photo_identity import PhotoIdentity


class Area:
    def __init__(self, area_deletion=AreaDeletion(), area_name=AreaName(), area_type=AreaType(),
                 area_latitude=AreaLatitude(), area_longitude=AreaLongitude(), parent_identity=ParentIdentity(),
                 photo_identity=PhotoIdentity(), area_identity=AreaIdentity()):
        self.area_identity = area_identity
        self.area_deletion = area_deletion
        self.area_name = area_name
        self.area_type = area_type
        self.area_latitude = area_latitude
        self.area_longitude = area_longitude
        self.parent_identity = parent_identity
        self.photo_identity = photo_identity
