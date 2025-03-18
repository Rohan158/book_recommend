from django.urls import path
from .views import search_books, recommend_books

urlpatterns = [
    path('search/', search_books, name='search_books'),  # /books/search/?q=python
    path('recommend/<str:genre>/', recommend_books, name='recommend_books'),  # /books/recommend/Fantasy
]
