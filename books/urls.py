from django.urls import path
from .views import search_books, recommend_books  
urlpatterns = [
    path('search/', search_books, name='search_books'),  # Matches `search_books` in views.py
    path('recommend/<str:genre>/', recommend_books, name='recommend_books'),  # Matches `recommend_books`
]
