
class Colour:
    def __init__(self, name='colour', alias="Colour", required=False, form_visible=False,
                 table_visible=False, value="", control='input', rank=0):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.rank = rank
