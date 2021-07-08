from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
       order_id = serializers.IntegerField(read_only=True)
       class Meta:
              model = Order
              fields = ['id', 'client', 'mobile', 'address', 'paid', 'status', 'total_price']