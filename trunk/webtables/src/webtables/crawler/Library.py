# -*- coding: utf-8 -*-

class Library:
    @classmethod
    def url_open(cls, url):
        url = Library.url_escape(url)
        print url
    
    @classmethod
    def url_escape(cls, url):
        return url
    
Library.url_open('http://en.wikipedia.org/wiki/Freedom_Road_Socialist_Organization_(Fight_Back!)')

from webtables.core.Filter import *

url = 'http://en.wikipedia.org/wiki/Freedom_Road_Socialist_Organization_(Fight_Back!)'
url = 'http://en.wikipedia.org/wiki/Freakazoid!_episode_list'
url = 'http://en.wikipedia.org/wiki/!!!Fuck_You!!!'
filter = Filter()

html = filter.urlopen(url)
print html