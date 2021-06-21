from django.urls import path
from . import views

urlpatterns = [
       path('books/', views.BookView.as_view()),
       path('authors/', views.AuthorView.as_view()),
       path('categories/', views.CategoryView.as_view()),
]