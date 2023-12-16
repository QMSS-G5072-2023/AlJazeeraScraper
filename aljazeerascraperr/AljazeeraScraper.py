#!/usr/bin/env python
# coding: utf-8

# In[13]:


from bs4 import BeautifulSoup 
from datetime import datetime
from utils import WebDriverHelper, LoggingHelper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

# In[14]:


class AlJazeeraScraper:
    base_url = "https://www.aljazeera.com/"

    def __init__(self, url=None):
        self._url = url
        self._data = ''
        self._soup = None
        self.logger_helper = LoggingHelper()
        self.logger = self.logger_helper.logger

        driver_path = os.getenv('CHROMEDRIVER_PATH', '/Users/peizhi/chromedriver-mac-x64/chromedriver')
        self.driver_helper = WebDriverHelper(driver_path)
        self.driver = self.driver_helper.init_web_driver()

    def requestPageUsingWebDriver(self, link):
        self.driver.get(link)
        self.driver.implicitly_wait(50)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        return soup

    def fetch_page(self, url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10) 
            return self.driver.page_source
        except Exception as e:
            # self.logger.error(f"Error fetching page: {e}")
            print(f"Error fetching page: {e}")
            return None

    def extract_category_urls(self):
        page_content = self.fetch_page(self.base_url)
        if page_content:
            soup = BeautifulSoup(page_content, "html.parser")
            nav_tag = soup.find('nav', class_='site-header__navigation css-15ru6p1')
            if nav_tag:
                li_tags = nav_tag.find_all('li', class_='menu__item menu__item--aje')
                categories = {
                    a.text.strip(): f"{self.base_url.rstrip('/')}/{a['href'].lstrip('/')}"
                    for li in li_tags for a in li.find_all('a', href=True)}
                return categories
        else:
    
            return {}

    def extract_latest_articles(self, category_url, max_articles=None, since_date=None):
        page_content = self.fetch_page(category_url)
        if page_content:
            soup = BeautifulSoup(page_content, "html.parser")
            result_links = []
            for a_tag in soup.find_all("a", class_='u-clickable-card__link'):
                if a_tag and "page" not in a_tag["href"] and "https" not in a_tag["href"]:
                    result_links.append(f'{self.base_url}{a_tag["href"]}')
            return result_links
        else:
            return []

    def close_driver(self):
        if self.driver:
            self.driver.quit()

