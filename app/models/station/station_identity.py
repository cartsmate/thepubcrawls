from app.static.pythonscripts.uuid import Uuid


class StationIdentity:
    def __init__(self, name='station_identity', alias="Id", required='false', form_visible='false',
                 table_visible='false', value=0, control='none'):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.alias = alias
        self.value = value
        self.control = control
