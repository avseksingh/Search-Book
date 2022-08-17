from django.urls import path
from . import views

urlpatterns = [
    path ('', views.booksearch, name = 'booksearch'),

    ]