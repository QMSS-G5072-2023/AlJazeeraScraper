#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
import pandas as pd
from aljazeerascraperr.AljazeeraScraper import AlJazeeraScraper

def test_aljazeera_scraper():
    scraper = AlJazeeraScraper()

    # Test extracting category URLs
    categories = scraper.extract_category_urls()
    assert isinstance(categories, dict), "Categories should be a dictionary"
    
    # Test extracting articles from a specific category
    economy_category_url = categories.get('Economy')
    assert economy_category_url is not None, "Economy category URL not found"
    
    latest_economy_articles = scraper.extract_latest_articles(economy_category_url)
    assert isinstance(latest_economy_articles, list), "Latest articles should be a list"
    assert len(latest_economy_articles) > 0, "Should have at least one latest article in Economy category"

    # Optional: Test scraping multiple articles and converting to DataFrame
    articles_data = scraper.scrapeMultipleArticles(latest_economy_articles)
    df = pd.DataFrame(articles_data)
    assert not df.empty, "DataFrame should not be empty"

    # Clean up: Close the WebDriver
    scraper.close_driver()

if __name__ == "__main__":
    pytest.main()