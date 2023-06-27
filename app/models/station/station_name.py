
class StationName:
    def __init__(self, name='station_name', required=True, form_visible=False, table_visible=False,
                 alias=None, value="", control='input'):
        self.name = name
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.alias = alias
        self.value = value
        self.control = control
