from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import User, Anime
from api.serializers import UserSerializer, AnimeSerializer

class UsersController(APIView):
  def get(self, request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      if (User.objects.filter(email=request.data['email']).exists()): # VERIFICA SE O USUÁRIO JÁ ESTÁ CADASTRADO.
        return Response({'error': 'Email already exists'}, status=status.HTTP_401_UNAUTHORIZED)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimesController(APIView):
  def get(self, request):
    animes = Anime.objects.all()
    serializer = AnimeSerializer(animes, many=True)
    return Response(serializer.data)
  

  