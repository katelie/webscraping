
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import random




# # # Chapter 3
url = "http://en.wikipedia.org"

def openPage(url):
    try: 
        html = urlopen(url)
    except HTTPError as e: 
        return None

    try:
        bsObj = BeautifulSoup(html, "html.parser")
    except AttributeError as e: 
        return None

    return bsObj



def getLinks(articleName):
    bsObj = openPage(url+articleName)

    try: 
        artilinks = bsObj.find('div', {'id':'bodyContent'}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        return None

    return artilinks

links = getLinks('/wiki/Ennio_Morricone')
while len(links) > 20: 
    newarticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newarticle)
    links = getLinks(newarticle)



# # # Chapter 1-2

# url = "http://www.pythonscraping.com/pages/warandpeace.html"

# def open_getTitle(url):
#     try: 
#         html = urlopen(url)
#     except HTTPError as e: 
#         return None

#     try:
#         bsObj = BeautifulSoup(html, "html.parser")
#         title = bsObj.body.h1
#     except AttributeError as e: 
#         return None

#     return bsObj, title


# bsObj, title = open_getTitle(url)

# print(title.get_text())

# names = bsObj.findAll("span", {"class":"green"})

# for name in names: 
#     print(name.get_text())




