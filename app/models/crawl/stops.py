from app.static.pythonscripts.uuid import Uuid


class Stops:
    def __init__(self, name='stops', alias="Id", required=False, visible=False, value=0, control="dropdown"):
        self.name = name
        self.alias = alias
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
