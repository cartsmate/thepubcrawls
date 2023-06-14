from app.static.pythonscripts.uuid import Uuid


class Quiz:
    def __init__(self, name="quiz", alias1="quiz", alias2="night", required=True, visible=False, value=False,
                 control="check", icon="quiz.png"):
        self.name = name
        self.alias1 = alias1
        self.alias2 = alias2
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
        self.icon = icon