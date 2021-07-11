from rest_framework import serializers
from .models import Order
from django.utils.translation import ugettext_lazy as _

class OrderSerializer(serializers.Serializer): 
       client_id = serializers.IntegerField(read_only=True)
       mobile = serializers.CharField(max_length=125)
       ordered_date = serializers.DateTimeField(read_only=True)
       address = serializers.CharField(max_length=125)
       paid = serializers.BooleanField(read_only=True) 
       status = serializers.CharField(read_only=True)
       total_price = serializers.FloatField(read_only=True)

       def create(self, validated_data):
              user =  self.context['request'].user
              return Order.objects.create(**validated_data,client=user)