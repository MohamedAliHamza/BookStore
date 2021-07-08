from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import ShopCart
from product.models import Book
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse

class ShopCartSerializer(serializers.Serializer):
    #book = serializers.SlugRelatedField(slug_field='name', read_only=True)
    #id = serializers.IntegerField(read_only=True)
    book_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(min_value=1, required=True)
    detail = serializers.SerializerMethodField()

    def create(self, validated_data):
        user =  self.context['request'].user
        book_id = validated_data.pop('book_id', None)
        quantity = validated_data.pop('quantity', None)
        book = get_object_or_404(Book, id=book_id)
        if user.shopcart_item.filter(book_id=book_id).exists():             
            raise serializers.ValidationError({"detail":_("This book already exist")})
        return ShopCart.objects.create(**validated_data, client=user, quantity=quantity, book=book)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

    def validate(self, attrs):
        book_id = attrs.get('book_id')
        quantity = attrs.get('quantity')
        book = get_object_or_404(Book, id=book_id)
        print(quantity)
        if quantity > book.stock_amount:
            raise serializers.ValidationError({"detail":_("This quantity is not in stock")})
        return attrs    
    def get_detail(self, obj):
        request = self.context['request']
        detail = {
            'link':reverse('shopcart-detail', kwargs={'pk':obj.id}, request=request)
        } 
        return detail