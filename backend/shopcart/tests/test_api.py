import pytest
from product.models import Category, Book, Author
from shopcart.models import ShopCart
from user.models import User
from shopcart.serializer import ShopCartSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from mixer.backend.django import mixer

client = APIClient()

@pytest.mark.django_db
class TestShopCart():

       @pytest.fixture
       def setup_shopcart(self):
              category = mixer.blend(Category)
              author1 = mixer.blend(Author)
              author2 = mixer.blend(Author)
              book1 = mixer.blend(Book, author=author1, category=category, quantity=5)
              book2 = mixer.blend(Book, author=author2, category=category)
              return  category, author1, author2, book1, book2

       
       def test_shopcart(self,setup_shopcart):
              user = User.objects.create_user(email='a@a.com', password='12345')
              data = {'email': 'a@a.com', 'password': '12345'}
              response = client.post(reverse('login'), data=data)
              access_token = response.json()['access']
              client2 = APIClient()
              client2.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
              data = {'book_id':setup_shopcart[3].id, 'quantity':3}
              response2 = client2.post(reverse('shopcart-list'), data=data)       
              assert response2.status_code == 201
              response2 = client2.get(reverse('shopcart-list'))
              assert response2.status_code == 200
