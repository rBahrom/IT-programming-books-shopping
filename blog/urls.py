from django.urls import path
from .views import books, auther, commit, home, alls, book_detail_view


urlpatterns = [
        path('', home, name='home'),
        path('books/', books, name='books'),
        path('auther/', auther, name='auther'),
        path('commit/', commit, name='commit'),
        path('alls/', alls, name='alls'),
        path('books/<int:id>/', book_detail_view, name='book-detail'),
]
