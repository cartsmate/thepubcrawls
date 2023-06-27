
class StationLongitude:
    def __init__(self, name='station_longitude', required=False, form_visible=False,
                 table_visible=False, alias=None, value=0, control=None):
        self.name = name
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.alias = alias
        self.value = value
        self.control = control
