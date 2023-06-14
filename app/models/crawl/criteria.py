
class Criteria:
    def __init__(self, name='criteria', required=True, visible=True, value="", alias=None, control="dropdown"):
        self.name = name
        self.required = required
        self.visible = visible
        self.value = value
        self.alias = alias
        self.control = control
