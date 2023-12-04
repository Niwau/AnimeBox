from rest_framework import serializers

class PushAnimeToListSerializer(serializers.Serializer):
  anime_id = serializers.IntegerField()
  list_id = serializers.IntegerField()

  def validate(self, data):
    if not data.get('list_id') or not data.get('anime_id'):
      raise serializers.ValidationError("list_id ou anime_id inválido")
    else:
      return data