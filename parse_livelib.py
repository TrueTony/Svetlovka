import requests
from requests import Session
from bs4 import BeautifulSoup
from gather_links import LinkFinder 

username = 'TrueTony'
wishlist = 'https://www.livelib.ru/reader/' + username + '/wish/print'

session = Session()
session.head(wishlist)
post = {
    'current_url': 'https://www.livelib.ru/',
    'user[login]': 'spanchbob@gmail.com',
    'user[onclick]': '',
    'user[password]': 'rubyb666',
    'user[redirect]': ''
}

link = requests.post('https://www.livelib.ru/', data=post)

link = requests.get('https://www.livelib.ru/')
#link.encoding = 'utf-8'

soup = BeautifulSoup(link.content, 'html.parser')

with open('test.txt', 'w') as f:
    f.write(soup.encode('utf-8'))
