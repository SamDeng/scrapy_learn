#http://www.cnblogs.com/fnng/p/3576154.html

import urllib
import re

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getimg(html):
    reg = r'src=


