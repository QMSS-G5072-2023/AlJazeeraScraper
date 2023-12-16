from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='aljazeerascraperr',  
    version='1.0.0',
    author='Peizhi Zhang',
    author_email='pz2277@columbia.edu',
    description='A Python package to scrape news articles from Al Jazeera.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/QMSS-G5072-2023/AlJazeeraScraper',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'selenium',
        "pandas"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

)