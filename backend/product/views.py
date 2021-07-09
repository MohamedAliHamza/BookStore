from rest_framework import generics
from .serializer import AuthorSerializer, CategorySerializer, BookSerializer
from .models import Author, Category, Book
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
    
class AuthorView(generics.ListAPIView):
       ''' API endpoint for listing authors '''
       queryset = Author.objects.all()
       serializer_class = AuthorSerializer
       permission_class =[]       

class AuthorDetailView(generics.RetrieveAPIView):
       ''' API endpoint for detail about specific author '''
       def get_object(self):
              slug = self.kwargs["slug"]
              obj = get_object_or_404(Author, slug=slug)
              return obj

       serializer_class = AuthorSerializer
       lookup_field = 'slug'
       lookup_url_kwarg = 'slug'        
       permission_class =[]      

class CategoryView(generics.ListAPIView):
       ''' API endpoint for listing categories '''
       queryset = Category.objects.all()
       serializer_class = CategorySerializer
       permission_class =[]       

class CategoryDetailView(generics.RetrieveAPIView):
       ''' API endpoint for detail about specific category '''
       def get_queryset(self):
              obj = self.kwargs['slug'] 
              return Book.objects.filter(category_slug=obj)

       serializer_class = BookSerializer
       permission_class =[]       

class BookView(generics.ListAPIView):
       ''' API endpoint for listing books '''
       queryset = Book.objects.filter(available=True) 
       serializer_class = BookSerializer
       permission_classes = []
