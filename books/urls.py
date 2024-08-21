from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.book_list, name='list'),
    path('<int:pk>/', views.book_detail, name='detail'),
    path('search/', views.search_books, name='search_books'),
    path('save_book/', views.save_book, name='save_book'),
    path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
]
