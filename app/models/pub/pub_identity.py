from app.static.pythonscripts.uuid import Uuid
import uuid


class PubIdentity:
    # def __init__(self, value):
    #     # name='pub_identity', alias="Id", required=False, form_visible=False,
    #     #          table_visible=False, value=uuid.uuid4(), control=None, icon=None):
    #     self.name = 'pub_identity'
    #     self.alias = "Pub Id"
    #     self.required = False
    #     self.form_visible = False
    #     self.table_visible = False
    #     self.value = value
    #     self.control = None
    #     self.icon = None
    def __init__(self, name='pub_identity', alias="Pub Id", required='false', form_visible='false',
                 table_visible='false', value='false', control='input', icon='false', rank=0):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
        self.rank = rank
