from app.static.pythonscripts.uuid import Uuid


class ReviewIdentity:
    def __init__(self, name='review_identity', alias="Review Id", alias2="", required=False, form_visible=False,
                 table_visible=False, value=Uuid().generate_uuid(), control=None, icon=None):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon