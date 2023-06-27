
class Postcode:
    def __init__(self, name='postcode', required=False, form_visible=False, table_visible=False, alias=None, value="",
                 control=None):
        self.name = name
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.alias = alias
        self.value = value
        self.control = control
