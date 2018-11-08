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
        time.sleep(3)
        page += 1
        upd_link = link + '~' + str(page)
        print(upd_link)
        r = requests.get(upd_link)
        soup = BeautifulSoup(r.content, 'lxml')
        books = soup.find_all('div', class_='brow-inner rback')

        for book in books:
            res = []
            title = book.find('a', class_='brow-book-name with-cycle')
            
            author = book.find('a', class_='brow-book-author')
            if author:
                res.append(author.text)
            else:
                res.append('Не установлен')
            res.append(title.text)
            links_of_books.append(res)

    with open('list_of_names.txt', 'w', encoding='utf-8') as f:
        for i in links_of_books:
            f.write(str(i) + '\n')

getting_books()