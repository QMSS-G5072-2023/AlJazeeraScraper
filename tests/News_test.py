#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from aljazeerascraperr.AljazeeraScraper import AlJazeeraScraper
scraper = AlJazeeraScraper()

try:
    # Extract category URLs
    categories = scraper.extract_category_urls()

    # Choose a category (for example, 'Economy')
    economy_category_url = categories.get('Economy')
    if economy_category_url:
        # Retrieve the latest articles from the Economy category
        latest_economy_articles = scraper.extract_latest_articles(economy_category_url)
        if latest_economy_articles:
            print("Latest Economy Articles:")
            for article in latest_economy_articles:
                print(article)
        else:
            print("No articles found in the Economy category.")
    else:
        print("Economy category URL not found")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the WebDriver
    scraper.close_driver()

