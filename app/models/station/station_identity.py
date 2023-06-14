from app.static.pythonscripts.uuid import Uuid


class StationIdentity:
    def __init__(self, name='station_identity', alias="Id", required=False, visible=False, value=0,
                 control=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.visible = visible
        self.alias = alias
        self.value = value
        self.control = control
