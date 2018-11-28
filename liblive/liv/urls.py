from django.urls import path
from . import views


app_name = 'liv'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('books/', views.BooksView.as_view(), name='books'),
    path('genres/', views.GenresView.as_view(), name='genres')
]