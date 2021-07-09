from rest_framework import serializers
from .models import Book, Category, Author
from user.serializer import UserSerializer
from rest_framework.reverse import reverse
from user.models import User

'''
I do not need `ModelSerializer` because all operations `CRUD` except `Read` I will do it from admin pannel.
'''
class AuthorSerializer(serializers.Serializer):
       name = serializers.CharField(max_length=100)  
       brief = serializers.CharField(style={'base_template': 'textarea.html'})
       number_of_books = serializers.IntegerField(default=0)
       image = serializers.FileField()

class CategorySerializer(serializers.Serializer):
       name = serializers.CharField(max_length=100)
       detail = serializers.SerializerMethodField('get_links')

       def get_links(self, obj): 
              request = self.context['request']
              return {
                     'category detail': reverse('category-detail',
                     kwargs={'pk': obj.pk}, request=request),
                     }

class BookSerializer(serializers.Serializer):
       #id = serializers.IntegerField() 
       name = serializers.CharField(max_length=100)
       description = serializers.CharField(style={'base_template': 'textarea.html'})
       category = serializers.SlugRelatedField(slug_field='name', read_only=True) 
       added_by = serializers.SlugRelatedField(slug_field='email', read_only=True)
       author = serializers.SlugRelatedField(slug_field='name', read_only=True)
       # ERROR: Return book slug instead of author slug 
       #author = serializers.HyperlinkedIdentityField(view_name='author-detail',lookup_field = 'slug')
       stock_amount = serializers.IntegerField()
       available = serializers.BooleanField()
       image = serializers.FileField()
       price = serializers.FloatField()