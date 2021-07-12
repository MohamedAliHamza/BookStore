from django.shortcuts import render
from rest_framework import generics
from .serializer import UserSerializer
from .models import User

class SignUpView(generics.CreateAPIView):
       ''' API endpoint for user to signup '''
       serializer_class = UserSerializer
       permission_classes = []

class UpdateUserView(generics.RetrieveUpdateAPIView):
       ''' API endpoint for user to update his info '''
       def get_object(self, queryset=None):
              obj = self.request.user
              return obj

       serializer_class = UserSerializer

