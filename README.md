### API SCRAPER FOR ALJAZEERA NEWS

### Description:

This python package is dedicated to scrape and parse all information from the interactive website of AlJazeera using selenium and webdriver. Users can fetch any news links and contents from the package with the appropriate version of webdriver and selenium package installed. As AlJazeeraScraper is the first scraper package for AlJazeera, it can contribute immensely to research, journalism, and sentiment analysis. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Dependencies](#dependencies)

## Installation

The scraper utilizes Selenium WebDriver, which requires a compatible WebDriver executable (like ChromeDriver) installed on your system. The test.py file used Selenium "^ 4.0 and chromedriver (Version: 120.0.6099.71 (r1217362)) that works for mac-armx64, from https://googlechromelabs.github.io/chrome-for-testing/.  Ensure that the WebDriver is correctly set up and configured for your environment. Always close the WebDriver using close_driver() to prevent resource leakage. Exception handling is crucial for a smooth and error-free scraping experience. 

## Usage

The `AlJazeeraScraper` class is designed to scrape and retrieve news articles from the Al Jazeera website. Below is a step-by-step guide on how to use it to obtain the latest articles from the "Economy" category.

Here's a quick guide on using it:

1. Instantiate the scraper: `scraper = AlJazeeraScraper()`.
2. Get URLs for news categories: `categories = scraper.extract_category_urls()`.
3. Find the URL for the Economy category: `economy_category_url = categories.get('Economy')`.
4. Fetch the latest Economy articles: `latest_economy_articles = scraper.extract_latest_articles(economy_category_url)`.
5. Iterate over `latest_economy_articles` to access individual article URLs.

Remember to close the WebDriver after use: `scraper.close_driver()`.

This simple process retrieves the latest articles from the Economy section of Al Jazeera, demonstrating the scraper's functionality.

## Contributing

We welcome contributions to our project. Please read our [Contributing Guidelines](./CONTRIBUTING.md) for more information on how to get involved.

## Code of Conduct

To ensure a welcoming and inclusive environment for all our contributors, please follow our [Code of Conduct](./CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](./LICENSE).

## Dependencies

[python = "^3.9"
praw = "^7.0"
pytest = "^7.4.3"
requests-mock = "^1.11.0"
selenium = "^4.0" 
webdriver-manager = "^3.5" ]