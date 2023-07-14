
class PubDeletion:
    def __init__(self, name='pub_deletion', alias="Delete", required=False, form_visible=False,
                 table_visible=False, value=False, control=None, rank=0):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.rank = rank
