import requests
from bs4 import BeautifulSoup


chooser = input("film: 1 \nseries: 2 \nwhich number? \n")
film = input("write directory \n")
req = requests.get("https://esubtitle.com/?s={0}/".format(film)).text
finder = BeautifulSoup(req, 'html.parser').find(text='دانلود زیرنویس فارسی سریال{0}'.format(film))
print(finder)