import time
import requests
from requests import Session
from bs4 import BeautifulSoup
import json


list_of_names = []
actual_in_lib = []
not_in_lib = []

with open('keys.txt', 'r') as f:
    data = json.load(f)
    for i in data:
        list_of_names.append(i)

for i in list_of_names:
    author = i[1][0]
    title = i[2]
    title = title.replace('(сборник)', '')
    title = title.split()
    key = i[7]
    
    book = '+'.join(title)
    
    url = f'http://opac.nekrasovka.ru/opacg2/?size=3&iddb=5&label0=FT&query0=&prefix1=AND&label1=TI&query1={book}&prefix2=AND&label2=AU&query2=&lang=&yearFrom=&yearTo=&_action=bibl%3Asearch%3Aadvanced'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    print(url)
    print(author)

    if soup.find('table', class_='biblSearchRecordsTable id_biblSearchRecordsTableContainer'):
        table = soup.find('table', class_='biblSearchRecordsTable id_biblSearchRecordsTableContainer')
        tbodys = soup.find_all('tbody')
        for tbody in tbodys[1:]:
            trs = tbody.tr.find_all('td')
            author = author.split()[-1]
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
                res.append(key)
                actual_in_lib.append(res)
                print(title, 'найдена')
    else:
        print(title, 'не найдена')
        not_in_lib.append([author, i[2]])


with open('actual_in_lib_text.txt', 'w', encoding='utf-8') as f:
    for i in actual_in_lib:
        f.write(str(i) + '\n')

with open('not_in_lib_text.txt', 'w', encoding='utf-8') as f:
    for i in not_in_lib:
        f.write(str(i) + '\n')

with open('actual_in_lib.txt', 'w') as f:
    json.dump(actual_in_lib, f)

with open('not_in_lib.txt', 'w') as f:
    json.dump(not_in_lib, f)