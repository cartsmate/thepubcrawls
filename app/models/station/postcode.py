
class Postcode:
    def __init__(self, name='postcode', required=False, visible=False, alias=None, value="",
                 control=None):
        self.name = name
        self.required = required
        self.visible = visible
        self.alias = alias
        self.value = value
        self.control = control
