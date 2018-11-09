import time
from selenium import webdriver
from seleniumrequests import Firefox
from bs4 import BeautifulSoup



links_of_books = []
list_of_books = []

webdriver = Firefox()

def close_up():

    with open('links_of_books.txt', 'r', encoding='utf-8') as f:
        with open ('list_of_books.txt', 'r', encoding='utf 8') as d:
            for link in f:
                print(link)
                link = link.replace('\n', '')
                if link not in d.read():
                    time.sleep(3)

                    r = webdriver.request('GET', link)
                    soup = BeautifulSoup(r.content, 'lxml')

                    with open('current_book.txt', 'w', encoding='utf-8') as f:
                        f.write(soup.prettify())

                    overview = []
                    overview.append(link)
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

                    with open('list_of_books.txt', 'a', encoding='utf-8') as f:
                        f.write(str(overview) + '\n')

                else:
                    print('Уже обработана', link)

close_up()