from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.anime_list import PushAnimeToListSerializer
from api.models import Anime, List

class AnimeListController(APIView):
  # ADICIONA UM ANIME A UMA LISTA.
  def post(self, request):
    serializer = PushAnimeToListSerializer(data=request.data)

    if (not serializer.is_valid()):
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      list = List.objects.filter(id=request.data['list_id'], user=request.user_id).first()

      if (list):
        anime = Anime.objects.filter(id=request.data['anime_id']).first()
        
        if (anime):
          list.animes.add(anime)
          return Response({'message': 'Anime adicionado à lista'}, status=status.HTTP_200_OK)
        else:
          return Response({'error': 'Anime não encontrado'}, status=status.HTTP_404_NOT_FOUND)
      else:
        return Response({'error': 'Lista não encontrada'}, status=status.HTTP_404_NOT_FOUND)