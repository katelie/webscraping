import os 
import re
from urllib.request import urlretrieve, urlopen 
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'

baseurl = 'http://cs229.stanford.edu/'


def getfullurl(base, addon):
    if type(addon) is not None:
        if addon.startswith("http://www."):
            url = "http://"+addon[11:]
        elif addon.startswith("http://"):
            url = addon
        elif addon.startswith("www."):
            url = "http://"+addon[4:]
        else: 
            url = base + "/" + addon

        if base not in url:
            return None

    return url


def openPage(url):
    try: 
        html = urlopen(url)
    except HTTPError as e: 
        return None

    try:
        obj = BeautifulSoup(html, "html.parser")
    except AttributeError as e: 
        return None

    return obj


def getDownloadPath(base, addon, ddir):
    path = addon.replace('www.','')
    path = path.replace(base,'')
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path


bsObj = openPage(getfullurl(baseurl,'materials.html'))
downloadList = bsObj.findAll("a",href=re.compile("[A-Za-z0-9\-\._]+\.pdf"))

# print(downloadList)

for pdffile in downloadList: 
    if 'http://' not in pdffile.attrs['href']:
        filepath = getfullurl(baseurl,pdffile.attrs['href'])

    # print(filepath)
        urlretrieve(filepath,getDownloadPath(baseurl,filepath,downloadDirectory))
