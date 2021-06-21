from .serializer import ShopCartItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import ShopCartItem
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class ShopCartItemListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
       user = self.request.user
       return ShopCartItem.objects.filter(client=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.is_valid(raise_exception=True)
        queryset = ShopCartItem.objects.filter(client=self.request.user,
                                               book=serializer.validated_data['book']).first()
        if queryset:
            if 'quantity' not in serializer.validated_data:
                queryset.quantity += 1
            else:
                queryset.quantity += serializer.validated_data['quantity']
            if queryset.quantity > queryset.product.min_stock_quantity:
                raise ValidationError("This quantity is not currently available")
            else:
                queryset.save()

        else:
            serializer.save(client=self.request.user)

    serializer_class = ShopCartItemSerializer


class ShopCartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopCartItem.objects.all()
    serializer_class = ShopCartItemSerializer
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
        book = get_object_or_404(ShopCartItem, pk=self.kwargs['pk']).book
        if 'quantity' not in serializer.validated_data:
            raise ValidationError("We need to enter quantity")
        elif serializer.validated_data['quantity'] > book.stock_amount:
            raise ValidationError("This quantity is not currently available")

        instance = serializer.save()
