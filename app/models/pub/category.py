
class Category:
    def __init__(self, name='category', alias="Category", required='true', form_visible='false',
                 table_visible='false', value="", control="dropdown", rank=0):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.rank = rank
