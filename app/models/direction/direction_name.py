
class DirectionName:
    def __init__(self, name='direction_name', alias=None, required=True, form_visible=True,
                 table_visible=True, value="", control='input'):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
