from django.shortcuts import render
from django.views import generic
from .models import Author, BookFromLivelib


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