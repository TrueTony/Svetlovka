from django.shortcuts import render
from django.views import generic
from .models import Author, BookFromLivelib, Genre, ActualBook
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumrequests import Firefox
import os


class IndexView(generic.ListView):
    template_name = 'liv/index.html'
    context_object_name = 'list_of_books'

    def get_queryset(self):
        return BookFromLivelib.objects.all()

class AuthorView(generic.ListView):
    template_name = 'liv/authors.html'
    context_object_name = 'list_of_authors'

    def get_queryset(self):
        return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'liv/author_detail.html'

class BooksView(generic.ListView):
    template_name = 'liv/books.html'
    context_object_name = 'list_of_books'

    def get_queryset(self):
        return BookFromLivelib.objects.all()

class BookDetailView(generic.DetailView):
    model = BookFromLivelib
    template_name = 'liv/book_detail.html'

class GenresView(generic.ListView):
    template_name = 'liv/genres.html'
    context_object_name = 'list_of_genres'

    def get_queryset(self):
        return Genre.objects.all()

class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = 'liv/genre_detail.html'

class LibView(generic.ListView):
    template_name = 'liv/lib.html'
    context_object_name = 'list_of_books'

    def get_queryset(self):
        return BookFromLivelib.objects.all()

@login_required
def MyView(request):
    # html = "<html><body>It is now 24.</body></html>"
    context = {
        'model': User
    }
    return render(request, 'liv/test.html', context)



@login_required
def addauthors(request):
    userlink = request.user.profile.link
    with open(f'list_of_books_{userlink}.txt', 'r') as f:
        data = json.load(f)
        for book in data:
            for author in book[1]:
                if not Author.objects.filter(name=author).exists():
                    a = Author()
                    a.name = author
                    a.save()
    
    print('Add Authors')

    return render(request, 'liv/test.html')

@login_required
def addgenres(request):
    userlink = request.user.profile.link
    with open(f'list_of_books_{userlink}.txt', 'r') as f:
        data = json.load(f)
        for book in data:
                for tag in book[3]:
                        if not Genre.objects.filter(name=tag).exists():
                            g = Genre()
                            g.name = tag
                            g.save()

    print('Add Genres')

    return render(request, 'liv/test.html')

@login_required
def addbooks(request):
    userlink = request.user.profile.link
    with open(f'list_of_books_{userlink}.txt', 'r') as f:
        data = json.load(f)
        for i in data:
            if not (BookFromLivelib.objects.filter(title=i[2]) and BookFromLivelib.objects.filter(author=Author.objects.get(name=i[1][0]))):
                b = BookFromLivelib()
                b.title = i[2]
                b.author = Author.objects.get(name=i[1][0])
                b.cover = i[4]
                b.rating = i[5]
                b.description = i[6]
                b.key = i[7]
                b.user = User.objects.get(username=request.user)
                b.save()

                # b = BookFromLivelib.objects.get(title=i[2])
                for g in i[3]:
                        genre = Genre.objects.get(name=g)
                        b.tags.add(genre)
                b.save()

    print('Add Books and Genres for Books')

    return render(request, 'liv/test.html')

@login_required
def addactualbooks(request):
    userlink = request.user.profile.link
    with open(f'actual_in_lib_{userlink}.txt', 'r') as f:
        data = json.load(f)
        for i in data:
            if not (ActualBook.objects.filter(title=i[1]) and ActualBook.objects.filter(author=i[0]) and ActualBook.objects.filter(notes=i[2])):
                a = ActualBook()
                a.author = i[0]
                a.title = i[1]
                a.notes = i[2]
                a.key = BookFromLivelib.objects.get(key=i[3])
                a.user = User.objects.get(username=request.user)
                a.save()
    
    print('Add ActualBooks')

    return render(request, 'liv/test.html')


@login_required
def getting_books(request):

    links_of_books = []

    userlink = request.user.profile.link
    link = f'https://www.livelib.ru/reader/{userlink}/wish/listview/smalllist/'
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    
    if soup.find('a', title='Последняя страница'): 
        num_of_pages = soup.find('a', title='Последняя страница')
    else:
        num_of_pages = 1

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

    with open(f'links_of_books_{userlink}.txt', 'w', encoding='utf-8') as f:
        for i in links_of_books:
            f.write(i + '\n')

    print('getting_books DONE!')

    return render(request, 'liv/test.html')

@login_required
def close_up(request):

    webdriver = Firefox()

    userlink = request.user.profile.link
    key = 0
    with open(f'links_of_books_{userlink}.txt', 'r', encoding='utf-8') as f:
        if not os.path.exists(f'list_of_books_{userlink}.txt'):
            open(f'list_of_books_{userlink}.txt', 'w', encoding='utf 8').close()
        with open (f'list_of_books_{userlink}.txt', 'r', encoding='utf 8') as d:
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
                    if os.stat(f'list_of_books_{userlink}.txt').st_size != 0:
                        with open(f'list_of_books_{userlink}.txt', 'r') as f:
                            old = json.load(f)
                            for i in old:
                                data.append(i)

                    data.append(overview)
                    with open(f'list_of_books_{userlink}.txt', 'w') as f:
                        json.dump(data, f)

                else:
                    print('Уже обработана', link)

    print('close_up DONE!')

    return render(request, 'liv/test.html')