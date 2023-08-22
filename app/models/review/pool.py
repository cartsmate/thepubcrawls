from app.static.pythonscripts.uuid import Uuid


class Pool:
    def __init__(self, name="pool", alias="pool", alias2="table", required='true', form_visible='false',
                 table_visible='false', value='false', control="check", icon="pool.png"):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
