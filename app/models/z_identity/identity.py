from app.static.pythonscripts.uuid import Uuid


class Identity:
    def __init__(self, name='identity', required=False, visible=False, value=Uuid().generate_uuid()):
        self.name = name
        self.required = required
        self.visible = visible
        self.value = value
