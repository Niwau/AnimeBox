from rest_framework import serializers
from api.models import Anime

class AnimeSerializer(serializers.HyperlinkedModelSerializer):
  image = serializers.ImageField(max_length=None, use_url=True)

  class Meta:
    model = Anime
    fields = ['name', 'sinopsis', 'image', 'id']

