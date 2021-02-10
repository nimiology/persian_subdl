import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

FILM = input("write film or series name \n")
REQ = requests.get("https://worldsubtitle.info/?s={0}".format(FILM)).text
try:
    LINK = BeautifulSoup(REQ, 'html.parser').find_all(title = FILM)
    ASLI = LINK[0]

except:
    print('\nsorry i cant find it plz choose number of these')
    LINK = BeautifulSoup(REQ,'html.parser').find_all(class_="cat-post-titel")
    for i in range(0,len(LINK)):
        print(f"{i+1} : {LINK[i].string}\n")
    CHoosed = int(input("\nchoose number! \n"))
    FILM = LINK[CHoosed-1].string
    print(FILM)
    ASLI=LINK[CHoosed-1]
    ASLI = BeautifulSoup(f'{ASLI}', 'html.parser').find_all('a')[0]


LINKPAGE = ASLI.get('href')
print(LINKPAGE)
REQ2 = requests.get(LINKPAGE).text
DOWNLOADLIST = BeautifulSoup(REQ2, 'html.parser').find_all(class_="new-link-3")

LINKSss =[]
for DOWNLOAD in DOWNLOADLIST:
    try:
        bs=BeautifulSoup(f'{DOWNLOAD}', 'html.parser').find_all('a')
        LINKSss.append(bs[0].get("href"))
    except:
        pass

for LINKk in LINKSss:
    try:
        NAME = []
        NAME.append(LINKk.split('/' ))
        NAME = NAME[0][-1]
        print(NAME)
        download_url(LINKk,f"Downloads/{NAME}")
        with ZipFile(f"Downloads/{NAME}", 'r') as zipObj:
            zipObj.extractall("Downloads/")
        os.remove(f"Downloads/{NAME}")

    except:
        print(NAME + " Failed")

