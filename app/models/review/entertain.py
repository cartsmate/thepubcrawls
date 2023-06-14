from app.static.pythonscripts.uuid import Uuid


class Entertain:
    def __init__(self, name="entertain", alias1="entertain", alias2="ment", required=True, visible=False, value=False,
                 control="check", icon="entertainment.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
