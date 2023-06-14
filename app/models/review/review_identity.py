from app.static.pythonscripts.uuid import Uuid


class ReviewIdentity:
    def __init__(self, name='review_identity', alias1="Id", alias2="", required=False, visible=False, value=Uuid().generate_uuid(),
                 control=None, icon=None):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon