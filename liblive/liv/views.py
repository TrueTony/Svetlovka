from django.shortcuts import render
from django.views import generic
from .models import Author, BookFromLivelib, Genre, ActualBook
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import json

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
    with open('list_of_books.txt', 'r') as f:
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
    with open('list_of_books.txt', 'r') as f:
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
    with open('list_of_books.txt', 'r') as f:
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
    with open('actual_in_lib.txt', 'r') as f:
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