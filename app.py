from nemweb.nemweb_scrape import NEMWebScraper
from nemweb.nemweb_store import NEMWebStore
from nemweb.nemweb_datasets import DATASETS

def app():
    nwsc = NEMWebScraper()
    nwst = NEMWebStore()
    for ds in [DATASETS['p5_min'], DATASETS['dispatch_is']]:
    	for res in nwsc.scrape(dataset=ds,start_date=nwst.START_DATE):
    		nwst.write(res)




if __name__ == '__main__':
    app()
