from rest_framework import serializers
from .models import Book, Category, Author
from user.serializer import UserSerializer

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)  
    brief = serializers.CharField(style={'base_template': 'textarea.html'})
    number_of_books = serializers.IntegerField(default=0)
    image = serializers.FileField()

class CategorySerializer(serializers.Serializer):
       name = serializers.CharField(max_length=100)

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    category = CategorySerializer()
    added_by = UserSerializer()
    author   = AuthorSerializer()
    stock_amount = serializers.IntegerField()
    image = serializers.FileField()
    price = serializers.FloatField()
