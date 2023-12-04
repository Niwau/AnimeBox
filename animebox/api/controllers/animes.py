from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import Anime
from api.serializers.anime import AnimeSerializer

class AnimesController(APIView):
  # RETORNA TODOS OS ANIMES DO SISTEMA.
  def get(self, request):
    animes = Anime.objects.all()
    serializer = AnimeSerializer(animes, many=True, context={'request': request})
    return Response(serializer.data)
  
  # CRIA UM NOVO ANIME.
  def post(self,  request):
    if (request.user_role != 'ADMIN'):
      return Response({'error': 'Você não tem permissão para criar um anime'}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = AnimeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)