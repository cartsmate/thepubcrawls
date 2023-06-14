
class Category:
    def __init__(self, name='category', alias="Category", required=True, visible=False, value="", control="dropdown"):
        self.name = name
        self.alias = alias
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
