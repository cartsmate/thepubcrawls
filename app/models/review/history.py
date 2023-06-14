from app.static.pythonscripts.uuid import Uuid


class History:
    def __init__(self, name="history", alias1="historic", alias2="venue", required=True, visible=False, value=False,
                 control="check", icon="castle.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
