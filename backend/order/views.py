from .models import Order
from rest_framework import generics

class OrderView(generics.ListCreateAPIView):
    ''' API endpoint for shopcart list, just owner can access it '''
       #serializer_class = 