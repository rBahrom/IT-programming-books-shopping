from django.urls import path
from .views import books, auther, commit, home, alls
urlpatterns = [
        path('', home, name='home'),
        path('books/', books, name='books'),
        path('auther/', auther, name='auther'),
        path('commit/', commit, name='commit'),
        path('alls/', alls, name='alls'),
]