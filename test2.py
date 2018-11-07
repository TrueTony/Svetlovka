import time
import requests
from requests import Session
from bs4 import BeautifulSoup

   
author = 'Коэльо'
book = 'Алхимик'
url = f'http://opac.nekrasovka.ru/opacg2/?size=3&iddb=5&label0=FT&query0=&prefix1=AND&label1=TI&query1={book}&prefix2=AND&label2=AU&query2=&lang=&yearFrom=&yearTo=&_action=bibl%3Asearch%3Aadvanced'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')


table = soup.find('table', class_='biblSearchRecordsTable id_biblSearchRecordsTableContainer')

tbodys = soup.find_all('tbody')
print(len(tbodys))

for tbody in tbodys[1:]:
    trs = tbody.tr.find_all('td')

    if author in trs[1].text:
        res = []
        res.append(trs[1].text)
        res.append(trs[2].text)
        res.append(trs[3].text)
        print(res)



with open('test3.txt', 'w') as f:
    infile = table
    f.write(str(infile))