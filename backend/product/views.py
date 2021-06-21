from rest_framework import generics
from .serializer import AuthorSerializer, CategorySerializer, BookSerializer
from .models import Author, Category, Book
from rest_framework.permissions import AllowAny

class BookView(generics.ListAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_class =[]       

class AuthorView(generics.ListAPIView):
       queryset = Author.objects.all()
       serializer_class = AuthorSerializer
       permission_class =[]       

class CategoryView(generics.ListAPIView):
       queryset = Category.objects.all()
       serializer_class = CategorySerializer
       permission_class =[]       
