
class Place:
    def __init__(self, name='place', alias="Place", required=True, visible=False, value="", control=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
