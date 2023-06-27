from app.static.pythonscripts.uuid import Uuid


class PhotoIdentity:
    def __init__(self, name='photo_identity', required=False, form_visible=False, table_visible=False,
                 value=Uuid().generate_uuid(), control=None):
        self.name = name
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
