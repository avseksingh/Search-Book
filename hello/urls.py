from django.urls import path
from . import views

urlpatterns = [
    path ('', views.bookssearch, name = 'bookssearch'),
    path ('selflink', views.selflink, name = 'selflink'),

    ]