from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from secrets import compare_digest


# Create your views here.

def load(request):
    return render(request, 'load.html')

def login_view(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', context={'message': "username or password invalid"})
    return render(request, 'login.html')

def register_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password2 != password:
            return render(request, 'register.html', context={"message_password": 'Error password !!'})
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', context={"message": 'username already exists !!'})
            new_users = User(first_name=first_name, last_name=last_name, email=email, username=username)
            new_users.set_password(password)
            new_users.save()
            return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('register')
