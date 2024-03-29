from webtables.packages.BeautifulSoup.BeautifulSoup import BeautifulSoup
from xml.dom import minidom

class WikipediaExtractor():
    def __init__(self):
        pass
    
    def extract(self, table_soup):
        str = table_soup.prettify()
        
        dom = minidom.parseString(str)
        
        rows = dom.getElementsByTagName('tr')
        
        if table_soup.get('class') == 'navbox': return None
        if table_soup.get('class') == 'toc': return None
        
        str = table_soup.prettify()
                       
        dom = minidom.parseString(str)
        
        rows = dom.getElementsByTagName("tr")
        
        for tr in rows:
            cells = [e for e in tr.childNodes if isinstance(e, minidom.Element)]
            cells = filter(lambda x: x.tagName in ['td', 'th'], cells)
            
            for cell in cells:
                value = self.getCellValue(cell)
                print value, '\t',
                """
                try:
                    print value, '\t',
                except UnicodeEncodeError:
                    value = value.encode("iso-8859-1", 'replace')
                    #value = value.encode('utf-8', 'replace')
                    #print '{ErrEncode}', value
                    print value, '\t',
                """
            print
            
    def getCellValue(self, td_elem):
        values = []
        self._getCellValue(td_elem, values)
        
        return ' '.join(filter(None, values))
    
    def _getCellValue(self, elem, values):
        childs = elem.childNodes
        
        for child in childs:
            if child.nodeType == minidom.Node.TEXT_NODE:
                values += [child.data.strip()]
                
            if child.nodeType == minidom.Node.ELEMENT_NODE:
                # TODO: <sup> with link are meaningless tag. remove it.
                if child.tagName == "sup": continue
                
                self._getCellValue(child, values)