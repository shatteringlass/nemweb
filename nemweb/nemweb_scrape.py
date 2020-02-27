import datetime
import re
import requests

from io import BytesIO
from nemweb.nemfile_reader import NEMZipReader
from nemweb.nemweb_logging import logger

class NEMWebScraper:

    def __init__(self):
        self.base_url = "http://www.nemweb.com.au"
        self.section = "Reports/CURRENT"

    def scrape(
            self,
            dataset,
            start_date
    ):

        page = requests.get("{0}/{1}/{2}/".format(self.base_url,
                                                  self.section,
                                                  dataset.dataset_name))

        regex = re.compile("/{0}/{1}/{2}".format(self.section,
                                                 dataset.dataset_name,
                                                 dataset.nemfile_pattern))

        for match in regex.finditer(page.text):
            file_datetime = datetime.datetime.strptime(
                match.group(1), dataset.datetime_format)
            
            if file_datetime < start_date:
                continue
            
            link = match.group(0)
            response = BytesIO(requests.get(
                "{0}{1}".format(self.base_url, link)).content)
            nemfile = NEMZipReader(response).get_content()

            logger.info("{} {}".format(dataset.dataset_name, file_datetime))

            yield nemfile
