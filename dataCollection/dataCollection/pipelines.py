import csv
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from src.logger import logging

class PricePipeline:
    def process_item(self,item,spider):
        logging.info("data processing on price constraint")
        adapter = ItemAdapter(item)
        
        if adapter.get("price"):
            adapter["price"] = adapter["price"] / 100000
            return item
        else:
            logging.info(f"missing price in a record {item}")
            raise DropItem(f"Missing Price in {item}")
