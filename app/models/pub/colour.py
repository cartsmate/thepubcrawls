
class Colour:
    def __init__(self, name='colour', alias="Colour", required='false', form_visible='false',
                 table_visible='false', value="", control='input', rank=0):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.rank = rank
