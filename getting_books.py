import time
import requests
from bs4 import BeautifulSoup

links_of_books = []
list_of_books = []

def getting_books():
    username = 'TrueTony'
    link = f'https://www.livelib.ru/reader/{username}/wish/listview/smalllist/'
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    
    num_of_pages = soup.find('a', title='Последняя страница')
    num_of_pages = num_of_pages['href'].split('~')[-1]

    for page in range(int(num_of_pages)):
        page += 1
        upd_link = link + '~' + str(page)
        print(upd_link)
        r = requests.get(upd_link)
        soup = BeautifulSoup(r.content, 'lxml')
        books = soup.find_all('a', class_='brow-book-name with-cycle')

        for book in books:
            links_of_books.append('https://www.livelib.ru/' + book['href'])

    with open('links_of_books.txt', 'w') as f:
        for i in links_of_books:
            f.write(i + '\n')

getting_books()