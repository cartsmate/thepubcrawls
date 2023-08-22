from app.static.pythonscripts.uuid import Uuid


class Entertain:
    def __init__(self, name="entertain", alias="fun", alias2="games", required='true', form_visible='false',
                 table_visible='false', value='false',
                 control="check", icon="theatre.png"):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
