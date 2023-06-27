
class Rank:
    def __init__(self, name='rank', alias="Rank", required=False, form_visible=True,
                 table_visible=True, value=0, control='star'):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
