from django.urls import path
from . import views

urlpatterns = [
       path('books/', views.BookView.as_view()),
       path('authors/', views.AuthorView.as_view()),
       
       path('categories/', views.CategoryView.as_view(), name='categories'),

       path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
]