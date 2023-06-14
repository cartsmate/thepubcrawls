
class StationName:
    def __init__(self, name='station_name', required=True, visible=False, alias=None, value="",
                 control='input'):
        self.name = name
        self.required = required
        self.visible = visible
        self.alias = alias
        self.value = value
        self.control = control
