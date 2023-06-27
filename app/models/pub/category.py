
class Category:
    def __init__(self, name='category', alias="Category", required=True, form_visible=False,
                 table_visible=False, value="", control="dropdown"):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
