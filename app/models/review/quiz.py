from app.static.pythonscripts.uuid import Uuid


class Quiz:
    def __init__(self, name="quiz", alias="quiz", alias2="night", required='true', form_visible='false',
                 table_visible='false', value='false', control="check", icon="quiz.png"):
        self.name = name
        self.alias = alias
        self.alias2 = alias2
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
