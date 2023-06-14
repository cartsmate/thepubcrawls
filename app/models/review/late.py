from app.static.pythonscripts.uuid import Uuid


class Late:
    def __init__(self, name="late", alias1="open", alias2="late", required=True, visible=False, value=False,
                 control="check", icon="late.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
