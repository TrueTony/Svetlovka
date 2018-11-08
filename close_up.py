import time
import requests
from bs4 import BeautifulSoup



links_of_books = []
list_of_books = []



def close_up():
    for i in links_of_books[:5]:
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
        rating = book.find('span', itemprop='ratingValue').text
        overview.append(rating)
        description = book.p.text
        overview.append(description)

        list_of_books.append(overview)

    with open('list_of_books.txt', 'w') as f:
        for i in list_of_books:
            f.write(str(i) + '\n')

with open('links_of_books.txt', 'r') as f:
    for i in f:
        links_of_books.append(i)

# print(links_of_books)
close_up()