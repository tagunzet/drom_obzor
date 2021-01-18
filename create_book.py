from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import docx




resp = urllib.request.urlopen("http://www.drom.ru/reviews/toyota/vitz/")
soup = BeautifulSoup(resp)

linkmass = []
tmpmass = []

def getlink(page):
    resp = urllib.request.urlopen(page)
    soup = BeautifulSoup(resp)
    for link in soup.find_all('a', href=True):
        if  len(link['href']) == 46:
            #print(link['href'])
            linkmass.append(link['href'])

doc = docx.Document()
doc.add_paragraph('Здравствуй, мир!')
def getinfo():

    for linkofinfo in linkmass:
        resp = urllib.request.urlopen(linkofinfo)
        soup = BeautifulSoup(resp)
        soup.prettify()
        for name in soup.find_all("div", {"class": "b-fix-wordwrap"}):
            tmps = (str(name.get_text().strip()))
            print('good')
            par1 = doc.add_paragraph('Итак:')
            par1.add_run(tmps)





for link in soup.find_all('a', href=True):
    if  'page' in link['href'] :
        #print(link['href'])
        getlink(link['href'])



print(linkmass)
getinfo()
print(tmpmass)
doc.save('helloworld.docx')
