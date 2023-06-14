
class Zone:
    def __init__(self, name='zone', required=False, visible=False, alias=None, value=0,
                 control=None):
        self.name = name
        self.required = required
        self.visible = visible
        self.alias = alias
        self.value = value
        self.control = control
