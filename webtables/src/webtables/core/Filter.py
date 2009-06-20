# This class recognizes Tables in HTML code.

from webtables.packages.BeautifulSoup.BeautifulSoup import BeautifulSoup
import re
import urllib2

class Filter:
    def __init__(self):
        pass
    
    def urlopen(self, url):
        patt_web = re.compile(r'^(http://(.*))$', re.I)
        patt_file = re.compile(r'^file://(.*)$', re.I)
        
        m_web = patt_web.match(url)
        m_file = patt_file.match(url)
        
        if m_web:
            headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            request = urllib2.Request(m_web.group(1), None, headers)

            return urllib2.urlopen(request).read()
        elif m_file:
            fhndl = open(m_file.group(1), 'r')
            fcontent = fhndl.read()
            fhndl.close()

            return fcontent
        else:
            raise IOException, 'Invalid URL'

    # this recognizes tables
    def filtering(self, html):
        soup = BeautifulSoup(html)
        
        return soup.findAll('table')