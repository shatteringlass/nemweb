import dataset

from dateutil import tz

import datetime
import os

from nemweb.nemweb_logging import logger

class NEMWebStore():

    def __init__(self):
        self.START_DATE = self.get_start_date()
        self.DB_URI = 'sqlite:///nemweb.db'

    def read(self, dataset):
        pass

    def write(self, nemfile):
        with dataset.connect(self.DB_URI) as cnx:
            for table in nemfile:
                header, *rows = nemfile[table]
                for r in rows:
                    cnx[table].insert({k: v for (k, v) in zip(header, r)})
        logger.info("Write completed.")

    def get_start_date(self):
        return datetime.datetime.now()
