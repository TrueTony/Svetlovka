from django.contrib import admin
from .models import Author,BookFromLivelib, ActualBook

admin.site.register(Author)
admin.site.register(BookFromLivelib)
admin.site.register(ActualBook)