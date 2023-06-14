from app.static.pythonscripts.uuid import Uuid


class Favourite:
    def __init__(self, name="favourite", alias1="PC", alias2="favs", required=True, visible=False,  value=False,
                 control="check", icon="favourite.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
