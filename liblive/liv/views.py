from django.shortcuts import render
from django.views import generic
from .models import Author, BookFromLivelib, Genre


class IndexView(generic.ListView):
    template_name = 'liv/index.html'
    context_object_name = 'list_of_authors'

    def get_queryset(self):
        return Author.objects.all()

class BooksView(generic.ListView):
    template_name = 'liv/books.html'
    context_object_name = 'list_of_books'

    def get_queryset(self):
        return BookFromLivelib.objects.all()

class GenresView(generic.ListView):
    template_name = 'liv/genres.html'
    context_object_name = 'list_of_genres'

    def get_queryset(self):
        return Genre.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'liv/author.html'

class BookDetailView(generic.DetailView):
    model = BookFromLivelib
    template_name = 'liv/book_detail.html'