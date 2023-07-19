
class PubName:
    def __init__(self, name='pub_name', alias="name", required=True, form_visible=True,
                 table_visible=True, value="", control='input', rank=0):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.rank = rank
