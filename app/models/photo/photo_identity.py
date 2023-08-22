from app.static.pythonscripts.uuid import Uuid


class PhotoIdentity:
    def __init__(self, name='photo_identity', alias="Photo Id", required='false', form_visible='false', table_visible='false',
                 value=Uuid().generate_uuid(), control='none'):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
