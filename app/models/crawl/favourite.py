
class Favourite:
    def __init__(self, name='favourite', required=False, visible=False, value="", control="dropdown"):
        self.name = name
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
