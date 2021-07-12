from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
       email = serializers.EmailField()
       password = serializers.CharField(min_length=5, write_only=True)
       class Meta:
              model = User
              fields = ['email','password', 'mobile', 'full_name', 'address', 'avatar']
              
       def create(self, validated_data):
              password = validated_data.pop('password', None)
              instance = self.Meta.model(**validated_data)
              if password is not None:
                     instance.set_password(password)
              instance.save()
              return instance