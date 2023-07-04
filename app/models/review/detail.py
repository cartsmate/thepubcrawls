from app.static.pythonscripts.uuid import Uuid


class Detail:
    def __init__(self, name="detail", alias="Info", alias2="", required=False, form_visible=True,
                 table_visible=True, value=" ", control="input", icon=None):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
