from rest_framework import generics
from .serializer import AuthorSerializer, CategorySerializer, BookSerializer
from .models import Author, Category, Book
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

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

class CategoryDetail(generics.RetrieveAPIView):
       # def get_object(self, pk):
       #  return get_object_or_404(Category, pk)
       def get_queryset(self):
              return Book.objects.filter(category_id=lookup_field.pk)

       serializer_class = BookSerializer
       permission_class =[]       
