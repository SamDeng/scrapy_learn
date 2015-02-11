#http://www.cnblogs.com/fnng/p/3576154.html

import urllib
import re

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getimg(html):
    reg = r'src="(.+?\.jpg)" pic_ext' #
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

html = gethtml("http://www.taobao.com/market/nvbao/shouye.php?spm=1.7274553.201.31.TRCyFR")
print getimg(html)



