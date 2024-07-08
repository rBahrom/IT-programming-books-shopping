from django.shortcuts import render
from .models import Books, Auther, Commit

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
    auther = Auther.objects.all()
    return render(request, 'auther.html', {'auther': auther})

def commit(request):
    commit = Commit.objects.all()
    return render(request, 'commit.html', {'commit': commit})

def alls(request):
    return render(request, 'alls.html')
