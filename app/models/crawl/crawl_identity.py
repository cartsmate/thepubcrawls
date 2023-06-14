from app.static.pythonscripts.uuid import Uuid


class CrawlIdentity:
    def __init__(self, name='crawl_identity', alias="Id", required=False, visible=False, value=0, control=None):
        self.name = name
        self.alias = alias
        self.required = required
        self.visible = visible
        self.value = value
        self.control = control
