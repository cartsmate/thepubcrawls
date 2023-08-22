from app.static.pythonscripts.uuid import Uuid


class History:
    def __init__(self, name="history", alias="history", alias2="venue", required='true', form_visible='false',
                 table_visible='false', value='false', control="check", icon="history.png"):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
