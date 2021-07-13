from user.models import User
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from django.urls import reverse
from user.serializer import UserSerializer
import pytest
import json

client = APIClient()

@pytest.mark.django_db
class TestUser():

       def test_signup(self):
              # Test successful sign up
              response = client.post(reverse('signup'), data={'email': 'a@a.com', 'password': '12345'})
              assert response.status_code == 201
              assert User.objects.count() == 1

              # Test failed sign up with invalid password
              response = client.post(reverse('signup'), data={'email': 'a@a.com', 'password': '1234'})
              assert response.status_code == 400


       def test_login(self):
              user = User.objects.create_user(email='a@a.com', password='12345')
              assert User.objects.count() == 1 
              data = {'email': 'a@a.com', 'password': '12345'}
              response = client.post(reverse('login'), data=data)
              assert response.status_code == 200


       def test_update_user(self):
              user = User.objects.create_user(email='a@a.com', password='12345')
              assert User.objects.count() == 1
              data = {'email': 'a@a.com', 'password': '12345'}
              response = client.post(reverse('login'), data=data)
              assert response.status_code == 200
              self.access_token = response.json()['access']
              client2 = APIClient()
              client2.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
              response = client2.get(reverse('update'))
              assert response.status_code == 200
              serializer = UserSerializer(user)
              assert response.data == serializer.data
              assert response.json()['mobile'] == None
              # Test update mobile 
              response = client2.patch(reverse('update'), data={'mobile':'+201021546535'})
              assert response.json()['mobile'] == '+201021546535'
              assert response.status_code == 200

