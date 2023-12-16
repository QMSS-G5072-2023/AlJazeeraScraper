#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from aljazeerascraper.AljazeeraScraper import AlJazeeraScraper

class AlJazeeraClient:
    def __init__(self, driver_path=None):
        self.scraper = AlJazeeraScraper()

    def extract_categories(self):
        return self.scraper.extract_category_urls()

    def extract_latest_articles(self, category_url, max_articles=None, since_date=None):
        return self.scraper.extract_latest_articles(category_url, max_articles, since_date)

    def close(self):
        self.scraper.close_driver()

