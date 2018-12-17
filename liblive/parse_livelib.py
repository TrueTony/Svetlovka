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

    with open(f'links_of_books_{username}.txt', 'w', encoding='utf-8') as f:
        for i in links_of_books:
            f.write(i + '\n')

def close_up():
    key = 0
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
                    author = []
                    if book.find('h2', class_='author-name unreg'):
                        authors = book.find('h2', class_='author-name unreg')
                        names = authors.find_all('a')    
                        for name in names:
                            author.append(name.text)
                        overview.append(author)
                    else:
                        author.append('Сборник')
                        overview.append(author)
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
                    overview.append(key)
                    key += 1

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

getting_books()
close_up()