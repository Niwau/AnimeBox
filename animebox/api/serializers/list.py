from rest_framework import serializers
from api.serializers.anime import AnimeSerializer
from api.models import List

class ListSerializer(serializers.ModelSerializer):
  animes = AnimeSerializer(many=True, read_only=True)

  class Meta:
    model = List
    fields = ['name', 'animes', 'id']

class CreateListSerializer(serializers.ModelSerializer):
  def create(self, validated_data):
    user_id = self.context['request'].user_id
    list = List.objects.create(user_id=user_id, **validated_data)
    return list

  class Meta:
    model = List
    fields = ['name']