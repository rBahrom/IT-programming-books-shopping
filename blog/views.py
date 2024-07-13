from django.shortcuts import render
from .models import Books, Auther, Commit
from django.contrib.auth.decorators import login_required

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

@login_required
def auther(request):
    auther = Auther.objects.all()
    return render(request, 'auther.html', {'auther': auther})

@login_required
def commit(request):
    commit = Commit.objects.all()
    return render(request, 'commit.html', {'commit': commit})

def alls(request):
    return render(request, 'alls.html')


@login_required
def book_detail_view(request, id):
    book = Books.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})
