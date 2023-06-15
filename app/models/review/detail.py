from app.static.pythonscripts.uuid import Uuid


class Detail:
    def __init__(self, name="detail", alias1="Info", alias2="", required=False, visible=True, value="",
                 control="input", icon=None):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
