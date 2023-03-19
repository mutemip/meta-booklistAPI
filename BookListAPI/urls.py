from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_view, name="books"),
    path('books-list/', views.books, name="books-list")
]