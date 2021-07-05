from user.models import User
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from django.urls import reverse
import pytest
import json

client = APIClient()

@pytest.mark.django_db
class TestUser():
       
       @pytest.fixture
       def setup_user(self):
              user = mixer.blend(User, email='a@a.com')
              user.set_password('1')
              user.save()
              return user

       def test_login(self, setup_user):
              assert User.objects.count() == 1 
              data = {'email': 'a@a.com', 'password': '1'}
              response = client.post(reverse('login'), data=data)
              assert response.status_code == 200