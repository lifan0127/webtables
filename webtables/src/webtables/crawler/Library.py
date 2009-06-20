import re
import urllib2

class Library:   
    # patterns for URL
    patt_web = re.compile(r'^(http://(.*))$', re.I)
    patt_file = re.compile(r'^file://(.*)$', re.I)
    
    @classmethod
    def urlopen(cls, url):       
        m_web = cls.patt_web.match(url)
        m_file = cls.patt_file.match(url)
        
        if m_web:
            headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            request = urllib2.Request(m_web.group(1), None, headers)

            return urllib2.urlopen(request).read()
        elif m_file:
            print m_file.group(1)
            fhndl = open(m_file.group(1), 'r')
            fcontent = fhndl.read()
            fhndl.close()

            return fcontent
        else:
            raise IOException, 'Invalid URL'

    @classmethod
    def fixhtml(cls, url):
        pass