import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
from persian import PERSSIAN

lan = "Choose your language: \n per : persian\n"
LANGUAGE = input(lan)
FILM = input("write film or series name \n")

if LANGUAGE == "per":
    LINKSss = PERSSIAN(FILM)


def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)



for LINKk in LINKSss:
    try:
        NAME = []
        NAME.append(LINKk.split('/' ))
        NAME = NAME[0][-1]
        print(NAME)
        Downloaddirectory =f"Downloads/{NAME}"
        download_url(LINKk,Downloaddirectory)
        with ZipFile(Downloaddirectory, 'r') as zipObj:
            zipObj.extractall("Downloads/")
        os.remove(Downloaddirectory)

    except:
        print(NAME + " Failed")

