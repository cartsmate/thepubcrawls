from app.models.crawl.crawl_identity import CrawlIdentity
from app.models.crawl.crawl_deletion import CrawlDeletion
from app.models.crawl.criteria import Criteria
from app.models.crawl.favourite import Favourite
from app.models.crawl.start import Start
from app.models.crawl.stops import Stops
from app.models.crawl.walk import Walk


class Crawl:
    def __init__(self, crawl_identity=CrawlIdentity(), crawl_deletion=CrawlDeletion(), start=Start(), walk=Walk(),
                 favourite=Favourite(), stops=Stops(), criteria=Criteria()):
        self.crawl_identity = crawl_identity
        self.crawl_deletion = crawl_deletion
        self.criteria = criteria
        self.favourite = favourite
        self.start = start
        self.stops = stops
        self.walk = walk
