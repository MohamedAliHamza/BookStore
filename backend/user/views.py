from django.shortcuts import render
from rest_framework import generics
from .serializer import UserSerializer
from .models import User

class UserUpdateView(generics.RetrieveUpdateAPIView):
       def get_object(self, queryset=None):
              obj = self.request.user
              return obj
              
       serializer_class = UserSerializer

