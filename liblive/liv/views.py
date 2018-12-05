from django.shortcuts import render
from django.views import generic
from .models import Author, BookFromLivelib, Genre, ActualBook
from django.contrib.auth.models import User
from django.http import HttpResponse


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

def MyView(request):
    # html = "<html><body>It is now 24.</body></html>"
    context = {
        'model': User
    }
    return render(request, 'liv/tt.html', context)

