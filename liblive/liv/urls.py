from django.urls import path
from . import views


app_name = 'liv'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('authors/', views.AuthorView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', views.BooksView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('genres/', views.GenresView.as_view(), name='genres'),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('lib/', views.LibView.as_view(), name='libview')
    
]