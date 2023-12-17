#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import logging
import os
import ssl
from datetime import datetime

class WebDriverHelper:
    def __init__(self):
        self.options = self._setup_options()

    def _setup_options(self):
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        return options

    def init_web_driver(self):
        if os.environ.get('CI'):  # 'CI' environment variable in CI/CD environments
            service = Service(executable_path='chromedriver')
        else:
            # Path for local development
            path_to_chromedriver = '/Users/peizhi/chromedriver-mac-x64/chromedriver'
            service = Service(executable_path=path_to_chromedriver)

        driver = webdriver.Chrome(service=service, options=self.options)
        return driver

class LoggingHelper:
    def __init__(self, filename=None):
        if filename is None:
            filename = f"app_log_{datetime.now().strftime('%Y%m%d')}.log"
        self.filename = filename
        self.logger = self.set_custom_log_info()

    def set_custom_log_info(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            file_handler = logging.FileHandler(self.filename)
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger

    def report(self, exception):
        self.logger.exception(str(exception))


def verify_https_issue():
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
            getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

def get_last_scraped_time(filename):
    if not os.path.exists(filename):
        return -1
    file_time = os.path.getmtime(filename)
    now = datetime.timestamp(datetime.now())
    return int(round((now - file_time) / 60))

def check_cache(filename, cache_time):
    scraping_time = get_last_scraped_time(filename)
    return scraping_time < 0 or scraping_time > cache_time

