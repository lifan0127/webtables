from webtables.core.Filter import Filter
from webtables.core.extract.Extractor import Extractor
import webtables.library.BeautifulSoup.BeautifulSoup as BeautifulSoup

filter = Filter()
html = filter.urlopen('http://mojool.com/research/List_of_countries_by_carbon_dioxide_emissions_mod.html')

tables_soup = filter.filtering(html)

extractor = Extractor()

for table in tables_soup:
    print extractor.extract(table)