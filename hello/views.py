from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from .models import Greeting

# Create your views here.
def bookssearch(request):
    searchValue = ""
    b={}
    books = {}
    if request.GET:
        searchValue = request.GET["searchValue"]

        path = "https://www.googleapis.com/books/v1/volumes?q={0}".format(searchValue)
        # print(path)
        url = requests.get(path)
        # print(response.json())
        books = json.loads(url.text)
        print(len(books), type(books))
        for book in books:
            print(book)
        # b = json.dumps(books)
        b = books["items"]
        print(b)
    return render(request, "searchbook.html", {"books": b,"searchValue":searchValue})
        # return HttpResponse(json.dumps(books), content_type='application/json')
    return render(request, "searchbook.html")

def selflink(request):
    path= request.GET["path"]
    print(path ,"")
    url = requests.get(path)
    bookselflink = json.loads(url.text)
    # print(len(bookselflink))
    return render(request,"selflink.html",{"books":bookselflink})
    # return HttpResponse(json.dumps(bookselflink),content_type='application/json')


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
