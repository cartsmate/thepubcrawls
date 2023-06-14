from app.static.pythonscripts.uuid import Uuid


class Garden:
    def __init__(self, name="garden", alias1="beer", alias2="garden", required=True, visible=False, value=False,
                 control="check", icon="garden.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
