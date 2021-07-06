import pytest
from product.models import Category, Book, Author
from product.serializer import CategorySerializer, BookSerializer, AuthorSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from mixer.backend.django import mixer

client = APIClient()

@pytest.mark.django_db
class TestCategory():

       @pytest.fixture
       def setup_category(self):
              category1 = mixer.blend(Category)
              category2 = mixer.blend(Category)
              return category1, category2

       
       def test_create_category(self,setup_category):   
              assert Category.objects.count() == 2

       def test_category_list(self,setup_category):
              response = client.get(reverse('categories'))
              categories = Category.objects.all()
              serializer = CategorySerializer(categories, many=True)
              assert response.data == serializer.data
              assert response.status_code == 200

       def test_category_detail(self, setup_category):
              book = mixer.blend(Book, category=setup_category[0])
              response = client.get(reverse('category-detail', kwargs={'slug':setup_category[0].slug } ))    
              serializer = BookSerializer(book)
              assert response.status_code == 200
              assert response.data == serializer.data


@pytest.mark.django_db
class TestBook():

       @pytest.fixture
       def setup_book(self):
              book1 = mixer.blend(Book)
              book2 = mixer.blend(Book)
              return book1, book2

       def test_book_list(self, setup_book):
              response = client.get(reverse('book_list')) 
              assert response.status_code == 200
              books = Book.objects.all()
              serializer = BookSerializer(books, many = True)
              assert books.count() == 2
              assert response.data == serializer.data

@pytest.mark.django_db
class TestAuthor:
       @pytest.fixture
       def setup_author(self):
              return mixer.blend(Author), mixer.blend(Author)

       def test_author_list(self, setup_author):
              response = client.get(reverse('authors'))
              authors = Author.objects.all()
              serializer = AuthorSerializer(authors, many=True)
              assert response.status_code == 200
              assert authors.count() == 2
              assert response.data == serializer.data

