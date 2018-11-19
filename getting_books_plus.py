import time
from selenium import webdriver
from seleniumrequests import Firefox
from bs4 import BeautifulSoup
import os
import json


webdriver = Firefox()

def close_up():

    with open('links_of_books.txt', 'r', encoding='utf-8') as f:
        with open ('list_of_books.txt', 'r', encoding='utf 8') as d:
            list_of_books = d.read()
            for link in f:
                print(link)
                link = link.replace('\n', '')
                if link not in list_of_books:
                    time.sleep(31)

                    r = webdriver.request('GET', link)
                    soup = BeautifulSoup(r.content, 'lxml')

                    with open('current_book.txt', 'w', encoding='utf-8') as f:
                        f.write(soup.prettify())

                    overview = [link]
                  
                    book = soup.find('div', class_='block-border card-block')
                    if book.find('h2', class_='author-name unreg'):
                        authors = book.find('h2', class_='author-name unreg')
                        names = authors.find_all('a')
                        author = []
                        for name in names:
                            author.append(name.text)
                        overview.append(author)
                    else:
                        overview.append('Сборник')
                    title = book.span.text
                    overview.append(title)
                    tags = book.find_all('a', class_='label-genre')
                    list_of_tags = []
                    for tag in tags:
                        list_of_tags.append(tag.text)
                    overview.append(list_of_tags)
                    cover = book.find('img', id='main-image-book')['src']
                    overview.append(cover)
                    if book.find('span', itemprop='ratingValue'):
                        rating = book.find('span', itemprop='ratingValue').text
                    else:
                        rating = 0
                    overview.append(rating)
                    description = book.p.text
                    overview.append(description)

                    data = []
                    if os.stat("list_of_books.txt").st_size != 0:
                        with open('list_of_books.txt', 'r') as f:
                            old = json.load(f)
                            for i in old:
                                data.append(i)

                    data.append(overview)
                    with open('list_of_books.txt', 'w') as f:
                        json.dump(data, f)

                else:
                    print('Уже обработана', link)

close_up()