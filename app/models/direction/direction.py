
from app.models.direction.direction_identity import DirectionIdentity
from app.models.direction.direction_name import DirectionName
from app.models.direction.direction_deletion import DirectionDeletion


class Direction:

    def __init__(self, direction_identity=DirectionIdentity(), direction_name=DirectionName(),
                 direction_deletion=DirectionDeletion()):
        self.direction_identity = direction_identity
        self.direction_name = direction_name
        self.direction_deletion = direction_deletion
