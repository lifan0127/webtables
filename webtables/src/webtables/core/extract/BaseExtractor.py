# This class extracts headers and data from Tables.

from webtables.library.BeautifulSoup.BeautifulSoup import BeautifulSoup
from xml.dom import minidom

class BaseExtractor:
    def __init__(self):
        pass
    
    def extract(self, table_soup):
        str = table_soup.prettify()
        
        dom = minidom.parseString(str)
        
        rows = dom.getElementsByTagName('tr')
        