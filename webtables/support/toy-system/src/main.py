import sys
sys.path.append('../../src/')

from webtables.crawler.Library import *
from webtables.packages.BeautifulSoup.BeautifulSoup import BeautifulSoup

html = Library.urlopen('file://../resources/htmls/List_of_countries_and_outlying_territories_by_area.html')


soup = BeautifulSoup(html)

tables_soup = soup.findAll('table')

from webtables.extractor.wikipedia.WikipediaExtractor import *

extractor = WikipediaExtractor()

for table in tables_soup:
    extractor.extract(table)