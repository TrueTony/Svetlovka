from django.shortcuts import render
from django.views import generic
from .models import Author


class IndexView(generic.ListView):
    template_name = 'liv/index.html'
    context_object_name = 'list_of_authors'

    def get_queryset(self):
        return Author.objects.all()