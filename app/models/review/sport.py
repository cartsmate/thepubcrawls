from app.static.pythonscripts.uuid import Uuid


class Sport:
    def __init__(self, name='sport', alias1="live", alias2="sports", required=True, visible=False, value=False,
                 control="check", icon="tv.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
