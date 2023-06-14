from app.static.pythonscripts.uuid import Uuid


class Dart:
    def __init__(self, name='dart', alias1="dart", alias2="board", required=True, visible=False, value=False,
                 control="check", icon="dart.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon