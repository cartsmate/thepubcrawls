from app.static.pythonscripts.uuid import Uuid


class StationIdentity:
    def __init__(self, name='station_identity', alias="Id", required=False, form_visible=False,
                 table_visible=False, value=0, control=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.alias = alias
        self.value = value
        self.control = control
