
class PubLatitude:
    def __init__(self, name="pub_latitude", alias="Latitude", required=True, form_visible=False,
                 table_visible=False, value=0, control=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
