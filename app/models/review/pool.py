from app.static.pythonscripts.uuid import Uuid


class Pool:
    def __init__(self, name="pool", alias1="pool", alias2="table", required=True, form_visible=False,
                 table_visible=False, value=False, control="check", icon="pool.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
