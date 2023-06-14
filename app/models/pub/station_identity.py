
class StationIdentity:
    def __init__(self, name='station_identity', alias="Station Id", required=False, visible=False, value=0, control=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
