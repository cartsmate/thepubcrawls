from app.static.pythonscripts.uuid import Uuid


class Music:
    def __init__(self, name="music", alias1="live", alias2="music", required=True, visible=False, value=False,
                 control="check", icon="music.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
