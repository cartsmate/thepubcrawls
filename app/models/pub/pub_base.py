import uuid
import abc


class BaseMeta(abc.ABCMeta):
    def __new__(mcs, name, bases, attrs):
        attrs['_class_uuid'] = uuid.uuid4()
        return super().__new__(mcs, name, bases, attrs)


class Base(metaclass=BaseMeta):
    def __init__(self, name='new_id', alias="Newid", required=False, form_visible=False,
                 table_visible=False, value=None, control=None, icon=None):
        print(self.__class__.__name__, self._class_uuid)
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        if value is None:
            value = self.__class__._class_uuid
        self.control = control
        self.icon = icon



class BaseNewId:
    def __new__(cls, new_id=uuid.uuid4()):
        return new_id


class NewId(BaseNewId):
    def __init__(self, name='new_id', alias="Newid", required=False, form_visible=False,
                 table_visible=False, value=uuid.uuid4(), control=None, icon=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.form_visible = form_visible
        self.table_visible = table_visible
        self.value = value
        self.control = control
        self.icon = icon
