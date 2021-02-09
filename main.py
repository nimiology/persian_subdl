import requests
from bs4 import BeautifulSoup


FILM = input("write directory \n")
REQ = requests.get("https://worldsubtitle.info/?s={0}".format(FILM)).text
LINK = BeautifulSoup(REQ, 'html.parser').find_all(title = FILM)
ASLI = LINK[0]
print(ASLI)
LINKPAGE = ASLI.get('href')
print(LINKPAGE)

REQ2 = requests.get(LINKPAGE).text
DOWNLOADLIST = BeautifulSoup(REQ2, 'html.parser').find_all(class_="new-link-3")

LINKS =[]
for DOWNLOAD in DOWNLOADLIST:
    bs=BeautifulSoup(f'{DOWNLOAD}', 'html.parser').find_all('a')
    print(bs)
    LINKS.append(bs[0].get("href"))

print(LINKS)

