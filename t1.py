import requests
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://www.commscope.com/ruckus/'
u = requests.get(url)
#avoid python-requests
#param = {
#    'page':'2'
#    'count':'5'
#}
#header = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
#}
#r = requests.post(url, params=param, headers=header)
#r = requests.get(url, auth=('123','123'), timeout=5)
if u.status_code == requests.codes.ok:
    soup = BeautifulSoup(u.text, "html.parser")
t1 = soup.find_all('p')
for t in t1:
    a = t.text
    if len(a)>0:
        print(t.text)
