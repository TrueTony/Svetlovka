import time
import requests
from requests import Session
from bs4 import BeautifulSoup


# session = Session()
# session.head()

book = 'тринадцатая+сказка'
url = f'http://opac.nekrasovka.ru/opacg2/?size=3&iddb=5&label0=FT&query0=&prefix1=AND&label1=TI&query1={book}&prefix2=AND&label2=AU&query2=&lang=&yearFrom=&yearTo=&_action=bibl%3Asearch%3Aadvanced'

post = {
    '_accept':	'html-snippet',
    '_action':	'bibl:search:quick',
    'data':	'result',
    'label':	'FT',
    'query':	'горе от ума'
}

r = requests.get(url)





soup = BeautifulSoup(r.content, 'lxml')

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

book = 'горе+от+ума'
url = f'http://opac.nekrasovka.ru/opacg2/?size=3&iddb=5&label0=FT&query0=&prefix1=AND&label1=TI&query1={book}&prefix2=AND&label2=AU&query2=&lang=&yearFrom=&yearTo=&_action=bibl%3Asearch%3Aadvanced'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

with open('test2.txt', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())