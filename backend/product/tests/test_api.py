import pytest
from product.models import Category, Book, Author
from product.serializer import CategorySerializer 
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