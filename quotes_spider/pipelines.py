# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class QuotesSpiderPipeline:
    def process_item(self, item, spider):
        tag = item.get('tags')
        
        if tag:
            item['tags'][0] = item['tags'][0].upper()
        return item
