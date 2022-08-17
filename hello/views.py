from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting

# Create your views here.
def booksearch(request):
    # return HttpResponse('Hello from Python!')
    searchValue = input("Enter search value\n")
    link = "https://www.googleapis.com/books/v1/volumes?q={0}".format(searchValue)
    print(link)
    response = requests.get(link)
    print(response.json())
    books = response.json()["items"]
    print(books)
    for book in books:
        print(book)
    return render(request, "searchbook.html", {"book":book})


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
