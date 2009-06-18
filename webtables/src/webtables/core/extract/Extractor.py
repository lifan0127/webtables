# This class extracts headers and data from Tables.

from webtables.library.BeautifulSoup.BeautifulSoup import BeautifulSoup
from xml.dom import minidom

class Extractor:
    def __init__(self):
        pass
    
    def extract(self, table_soup):
        str = table_soup.prettify()
        
        dom = minidom.parseString(str)
        
        trs = dom.getElementsByTagName("tr")
        
        selected_tr = trs[2]
        selected_td = selected_tr.getElementsByTagName("td")[1]
        
        self.get_cellvalue(selected_td)
        
    def get_cellvalue(self, td_element):
        #for item in td_element.childNodes:
        #    print item
        text = []
        self.traverse(td_element, text)
        
        print text
            
    def traverse(self, dom_element, text):
        childs = dom_element.childNodes
        
        for child in childs:
            if child.nodeType == minidom.Node.TEXT_NODE:
                #text = child.data.strip()
                #print child, text
                text += ['['+child.data+']']
                #print '-->', child.data.strip(), text
                #print child  
            
            if child.nodeType == minidom.Node.ELEMENT_NODE:
                #print child
                self.traverse(child, text)