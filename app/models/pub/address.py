
class Address:
    def __init__(self, name='address', alias="Address", required=True, visible=False, value="", control='input'):
        self.name = name
        self.alias = alias
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
