from django.urls import path

from .views import (login_view, register_view,
                    logout_view, load, account_view,
                    account_profile_view, shopping_books_view,
                    like_books_view

                    )

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('load/', load, name='load'),
    path('account/', account_view, name='account'),
    path('person/', account_profile_view, name='person'),
    path('shopping_books/', shopping_books_view, name='shopping_books'),
    path('like_books/', like_books_view, name='like_books'),

]
