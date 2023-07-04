from app.static.pythonscripts.uuid import Uuid


class Garden:
    def __init__(self, name="garden", alias="beer", alias2="garden", required=True, form_visible=False,
                 table_visible=False, value=False, control="check", icon="garden.png"):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
