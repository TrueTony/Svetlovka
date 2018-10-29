import time
import requests
from bs4 import BeautifulSoup


def getting_books():
    username = 'TrueTony'
    link = f'https://www.livelib.ru/reader/{username}/wish/listview/smalllist/'
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    num_of_pages = None
    while type(num_of_pages) != type('a'):
        num_of_pages = soup.find('a', title='Последняя страница')
        num_of_pages = num_of_pages['href'].split('~')[-1]
        print('getting number of pages')
        time.sleep(3)

    list_of_books = []

    for page in range(int(num_of_pages)):
        page += 1
        upd_link = link + '~' + str(page)
        print(upd_link)
        r = requests.get(upd_link)
        soup = BeautifulSoup(r.content, 'lxml')
        books = soup.find_all('a', class_='brow-book-name with-cycle')

        for book in books:
            list_of_books.append('https://www.livelib.ru/' + book['href'])

    with open('test.txt', 'w') as f:
        for i in list_of_books:
            f.write(i + '\n')
