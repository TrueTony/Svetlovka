from django.urls import path
from . import views


app_name = 'liv'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]