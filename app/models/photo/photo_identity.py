from app.static.pythonscripts.uuid import Uuid


class PhotoIdentity:
    def __init__(self, name='photo_identity', required=False, visible=False, value=Uuid().generate_uuid(),
                 control=None):
        self.name = name
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
