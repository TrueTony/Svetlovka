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
        time.sleep(2)
        page += 1
        upd_link = link + '~' + str(page)
        print(upd_link)
        r = requests.get(upd_link)
        soup = BeautifulSoup(r.content, 'lxml')
        books = soup.find_all('a', class_='brow-book-name with-cycle')

        for book in books:
            links_of_books.append('https://www.livelib.ru/' + book['href'])

    with open('links_of_books.txt', 'w', encoding='utf-8') as f:
        for i in links_of_books:
            f.write(i + '\n')

def close_up():
    for i in links_of_books:
        time.sleep(3)
        link = i
        print(link)
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')

        with open('current_book.txt', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        overview = []
        book = soup.find('div', class_='block-border card-block')
        name = book.span.text
        overview.append(name)
        tags = book.find_all('a', class_='label-genre')
        for tag in tags:
            overview.append(tag.text)
        cover = book.find('img', id='main-image-book')['src']
        overview.append(cover)
        if book.find('span', itemprop='ratingValue'):
            rating = book.find('span', itemprop='ratingValue').text
        else:
            rating = 0
        overview.append(rating)
        description = book.p.text
        overview.append(description)

        list_of_books.append(overview)

    with open('list_of_books.txt', 'w', encoding='utf-8') as f:
        for i in list_of_books:
            f.write(str(i) + '\n')

getting_books()
close_up()