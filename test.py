import requests
from requests import Session


session = Session()
url = 'https://www.livelib.ru/'
session.head(url)
post = {
    'current_url': 'https://www.livelib.ru/',
    'user[login]': 'spanchbob@gmail.com',
    'user[password]': 'rubyb666'
}

r = requests.post('https://www.livelib.ru/', data=post, headers={'Referer': url})

r.encoding = 'utf-8'
print(r.encoding)

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)