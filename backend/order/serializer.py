from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
       class Meta:
              model = Order
              fields = ['id', 'client', 'mobile', 'address', 'paid', 'status', 'total_price']