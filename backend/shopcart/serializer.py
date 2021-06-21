from rest_framework import serializers
from .models import ShopCartItem

class ShopCartItemSerializer(serializers.ModelSerializer):
    class Meta:
       model = ShopCartItem
       fields = '__all__'
