from django.shortcuts import render
from .models import Books

# Create your views here.


def home(request):
    return render(request, 'home.html')

def books(request):
    if request.method == 'POST':
        search = request.POST["search"]
        books = Books.objects.filter(title__icontains=search)
        return render(request, 'books.html', {'books': books})
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

def auther(request):
    return render(request, 'auther.html')

def commit(request):
    return render(request, 'commit.html')

def alls(request):
    return render(request, 'alls.html')
