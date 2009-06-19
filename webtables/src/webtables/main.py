from webtables.core.Filter import Filter
from webtables.core.extract.WikipediaExtractor import WikipediaExtractor
import webtables.library.BeautifulSoup.BeautifulSoup as BeautifulSoup

filter = Filter()

#url = 'http://mojool.com/research/List_of_countries_by_carbon_dioxide_emissions_mod.html'
#url = 'http://en.wikipedia.org/wiki/List_of_countries_by_population'
url = 'http://mojool.com/research/List_of_countries_by_population.html'

html = filter.urlopen(url)

tables_soup = filter.filtering(html)

extractor = WikipediaExtractor()

for table in tables_soup:
    extractor.extract(table)