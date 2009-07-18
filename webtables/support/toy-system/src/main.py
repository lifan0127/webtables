import sys
sys.path.append('../../src/')

from webtables.crawler.Library import *
from webtables.packages.BeautifulSoup.BeautifulSoup import BeautifulSoup

html = Library.urlopen('file://../resources/htmls/List_of_countries_and_outlying_territories_by_area.html')

import re

html = re.sub('&#160;', ' ', html)

soup = BeautifulSoup(html)

#div_soup = soup.find('div', {'id': 'bodyContent'})
div_soup = soup.find("div", {"id": "bodyContent"})

tables_soup = div_soup.findAll('table', recursive=False)

from webtables.extractor.wikipedia.WikipediaExtractor import *

extractor = WikipediaExtractor()

for table in tables_soup:
    extractor.extract(table)