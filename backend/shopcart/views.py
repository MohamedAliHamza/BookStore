from .serializer import ShopCartSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import ShopCart
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class ShopCartView(generics.ListCreateAPIView):
    ''' API endpoint for shopcart list, just owner can access it '''
    def get_queryset(self):
       user = self.request.user
       return ShopCart.objects.filter(client=user)

    serializer_class = ShopCartSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class ShopCartDetailView(generics.RetrieveUpdateDestroyAPIView):
    ''' API endpoint for shopcart detail, just owner can access it '''
    def get_object(self):
        return get_object_or_404(ShopCart, id=self.kwargs['pk'])
    serializer_class = ShopCartSerializer 
    permission_classes = [IsAuthenticated, IsOwner]