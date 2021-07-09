from django.urls import path
from . import views

urlpatterns = [
       # Author URLS
       path('authors/', views.AuthorView.as_view(), name='authors'),
       path('author/<slug:slug>/', views.AuthorDetailView.as_view(), name='author-detail'),

       # Category URLS
       path('categories/', views.CategoryView.as_view(), name='categories'),
       path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category-detail'),

       # Book URLS
       path('books/', views.BookView.as_view(), name='book_list'),

]