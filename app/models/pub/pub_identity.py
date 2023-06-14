from app.static.pythonscripts.uuid import Uuid


class PubIdentity:
    def __init__(self, name='pub_identity', alias="Id", required=False, visible=False, value=Uuid().generate_uuid(),
                 control=None, icon=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon
