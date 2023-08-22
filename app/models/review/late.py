from app.static.pythonscripts.uuid import Uuid


class Late:
    def __init__(self, name="late", alias="late", alias2="open", required='true', form_visible='false',
                 table_visible='false', value='false', control="check", icon="late.png"):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
