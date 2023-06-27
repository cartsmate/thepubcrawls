from app.static.pythonscripts.uuid import Uuid


class AreaIdentity:
    def __init__(self, name='area_identity', alias="Id", required=False, form_visible=False,
                 table_visible=False, value=0, control=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
