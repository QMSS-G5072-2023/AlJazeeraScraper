#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from aljazeerascraper.AljazeeraScraper import AlJazeeraScraper
from bs4 import BeautifulSoup
from selenium import webdriver
import os

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

    def fetch_page(self, url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10) 
            return self.driver.page_source
        except Exception as e:
            print(f"Error fetching page: {e}")
            return None

    def extract_category_urls(self):
        page_content = self.fetch_page(self.base_url)
        if page_content:
            soup = BeautifulSoup(page_content, "html.parser")
            nav_tag = soup.find('nav', class_='site-header__navigation css-15ru6p1')
            if nav_tag:
                li_tags = nav_tag.find_all('li', class_='menu__item menu__item--aje')
                categories = {}
                for li in li_tags:
                    for a in li.find_all('a', href=True):
                        text = a.text.strip()
                        href = a['href'].strip()
                        if href.startswith('http'):
                            categories[text] = href
                        else:
                            categories[text] = f"{self.base_url.rstrip('/')}/{href.lstrip('/')}"
                return categories
        else:
            return {}

    def extract_latest_articles(self, category_url, max_articles=20):
        page_content = self.fetch_page(category_url)
        if page_content:
            soup = BeautifulSoup(page_content, "html.parser")
            result_links = []
            for a_tag in soup.find_all("a", class_='u-clickable-card__link'):
                if a_tag and "page" not in a_tag["href"] and "https" not in a_tag["href"]:
                    result_links.append(f'{self.base_url.rstrip("/")}/{a_tag["href"].lstrip("/")}')
                    if len(result_links) >= max_articles:
                        break
            return result_links
        else:
            return []

    def scrapeMultipleArticles(self, links):
        articles = []
        for link in links:
            article = self.scrapeArticle(link)
            if article:
                articles.append(article)
        return articles

    def scrapeArticle(self, link):
        try:
            self.driver.get(link)
            self.driver.implicitly_wait(10)
            parsed_page = BeautifulSoup(self.driver.page_source, "html.parser")
            article_data = {"title": "", "author": "Al Jazeera", "date": "", "image_url": "", "content": ""}
            try:
                header = parsed_page.find('header', class_='article-header')
                article_data["title"] = header.find('h1').text if header and header.find('h1') else "No Title"
                author_info = parsed_page.find('div', class_='article-author-name')
                article_data["author"] = author_info.find('a', class_='author-link').text if author_info and author_info.find('a', class_='author-link') else "Unknown"
                date_info = parsed_page.find('div', class_='article-dates')
                article_data["date"] = date_info.find('span').text.strip() if date_info and date_info.find('span') else "Unknown"
                figure = parsed_page.find('figure', class_='article-featured-image')
                article_data["image_url"] = figure.find('img')['src'] if figure and figure.find('img') else ""
                content_area = parsed_page.find('div', class_='wysiwyg')
                paragraphs = [para.text for para in content_area.find_all('p')] if content_area else []
                article_data["content"] = "\n".join(paragraphs)
            except Exception as e:
                print(f"Error parsing article: {e}")
                return None
        except Exception as e:
            print(f"Error scraping article: {e}")
            return None
        return article_data
