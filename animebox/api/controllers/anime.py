from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import Anime
from api.serializers.anime import AnimeSerializer

class AnimeController(APIView):
  # RETORNA UM ANIME ESPECÍFICO.
  def get(self, request, anime_id):
    anime = Anime.objects.filter(id=anime_id).first()
    serializer = AnimeSerializer(anime, context={'request': request})
    return Response(serializer.data)

  # DELETA UM ANIME.
  def delete(self, request, anime_id):
    if (request.user_role != 'ADMIN'):
      return Response({'error': 'Você não tem permissão para remover um anime'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
      anime = Anime.objects.filter(id=anime_id).first()
      
      if (anime):
        anime.delete()
        return Response({'message': 'Anime removido'}, status=status.HTTP_200_OK)
      else:
        return Response({'error': 'Anime não encontrado'}, status=status.HTTP_404_NOT_FOUND)