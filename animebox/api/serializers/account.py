from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api.models import User

class AccountSerializer(serializers.HyperlinkedModelSerializer):
  def create(self, validated_data):
    password = validated_data.pop('password')
    hashed_password = make_password(password)
    user = User.objects.create(password=hashed_password, **validated_data)
    return user

  class Meta:
    model = User
    fields = ['name', 'email', 'password', 'role', 'id']

class UpdateAccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['name']

class AccountLoginSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'password']
