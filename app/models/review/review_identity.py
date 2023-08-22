from app.static.pythonscripts.uuid import Uuid


class ReviewIdentity:
    def __init__(self, name='review_identity', alias="Review Id", alias2="", required='false', form_visible='false',
                 table_visible='false', value=Uuid().generate_uuid(), control='none', icon='none'):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon