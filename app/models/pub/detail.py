from app.static.pythonscripts.uuid import Uuid


class Detail:
    def __init__(self, name="detail", alias="extra info", alias2="", required='false', form_visible='false',
                 table_visible='false', value="TBC", control="input", icon='false', rank=3):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
        self.rank = rank
