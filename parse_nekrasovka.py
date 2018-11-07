import time
import requests
from requests import Session
from bs4 import BeautifulSoup


list_of_names = []

with open('list_of_names.txt', 'r', encoding='utf-8') as f:
    for i in f:
        list_of_names.append(i)




for i in list_of_names:
    i = i.split('-')
    author = i[0]
    title = i[1].split()
    book = '+'.join(title)
    

    book = title
    url = f'http://opac.nekrasovka.ru/opacg2/?size=3&iddb=5&label0=FT&query0=&prefix1=AND&label1=TI&query1={book}&prefix2=AND&label2=AU&query2=&lang=&yearFrom=&yearTo=&_action=bibl%3Asearch%3Aadvanced'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
   
    print(book)

    try:
        table = soup.find('table', class_='biblSearchRecordsTable id_biblSearchRecordsTableContainer')

        with open(book + 'txt', 'w', encoding='utf8') as f

        tbodys = soup.find_all('tbody')

        for tbody in tbodys[1:]:
            trs = tbody.tr.find_all('td')

            if author in trs[1].text:
                res = []
                res.append(trs[1].text)
                res.append(trs[2].text)
                res.append(trs[3].text)
                print(res)
    except:
        print(book, 'не найдена')



