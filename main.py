import requests
from bs4 import BeautifulSoup


FILM = input("write directory \n")
REQ = requests.get("https://worldsubtitle.info/?s={0}".format(FILM)).text
try:
    LINK = BeautifulSoup(REQ, 'html.parser').find_all(title = FILM)
    ASLI = LINK[0]

except:
    print('sorry i cant find it plz choose number of these')
    LINK = BeautifulSoup(REQ,'html.parser').find_all(class_="cat-post-titel")
    for i in range(0,len(LINK)):
        print(f"{i+1} : {LINK[i].string}\n")
    CHoosed = int(input("\nchoose number! \n"))
    ASLI=LINK[CHoosed-1]
    ASLI = BeautifulSoup(f'{ASLI}', 'html.parser').find_all('a')[0]


LINKPAGE = ASLI.get('href')
print(LINKPAGE)
REQ2 = requests.get(LINKPAGE).text
DOWNLOADLIST = BeautifulSoup(REQ2, 'html.parser').find_all(class_="new-link-3")

LINKS =[]
for DOWNLOAD in DOWNLOADLIST:
    bs=BeautifulSoup(f'{DOWNLOAD}', 'html.parser').find_all('a')
    LINKS.append(bs[0].get("href"))

print(LINKS)

