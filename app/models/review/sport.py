from app.static.pythonscripts.uuid import Uuid


class Sport:
    def __init__(self, name='sport', alias="live", alias2="sports", required=True, form_visible=False,
                 table_visible=False, value=False, control="check", icon="tv.png"):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
