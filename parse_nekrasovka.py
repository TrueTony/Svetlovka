import time
import requests
from requests import Session
from bs4 import BeautifulSoup


list_of_names = []
actual_in_lib = []

with open('list_of_names.txt', 'r', encoding='utf-8') as f:
    for i in f:
        list_of_names.append(i)

for i in list_of_names:
    author = i[0]
    title = i[1].split()
    book = '+'.join(title)
    
    url = f'http://opac.nekrasovka.ru/opacg2/?size=3&iddb=5&label0=FT&query0=&prefix1=AND&label1=TI&query1={book}&prefix2=AND&label2=AU&query2=&lang=&yearFrom=&yearTo=&_action=bibl%3Asearch%3Aadvanced'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    if soup.find('table', class_='biblSearchRecordsTable id_biblSearchRecordsTableContainer'):
        table = soup.find('table', class_='biblSearchRecordsTable id_biblSearchRecordsTableContainer')
        tbodys = soup.find_all('tbody')
        for tbody in tbodys[1:]:
            trs = tbody.tr.find_all('td')
            if author in trs[1].text:
                res = []
                author = trs[1].text
                author = author.replace('\n', '')
                title = trs[2].text
                title = title.replace('\n', '')
                data = trs[3].text
                data = data.replace('\n', '')
                res.append(author)
                res.append(title)
                res.append(data)
                actual_in_lib.append(res)
                print(i, 'найдена')
    else:
        print(i, 'не найдена')


with open('actual_in_lib.txt', 'w', encoding='utf-8') as f:
    for i in actual_in_lib:
        f.write(str(i) + '\n')