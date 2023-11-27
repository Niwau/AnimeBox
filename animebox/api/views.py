from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import User, Anime, List, Comment
from api.serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer, AnimeSerializer, ListSerializer, UserLoginSerializer, CreateListSerializer, CommentSerializer, CreateCommentSerializer, EpisodeSerializer
from django.contrib.auth.hashers import check_password
from api.utils import create_user_token

class UsersController(APIView):
  def get(self, request):
    users = User.objects.get(id=request.user_id)
    serializer = UserSerializer(users)

    if (not users):
      return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

  def post(self, request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
      if (User.objects.filter(email=request.data['email']).exists()): # VERIFICA SE O USUÁRIO JÁ ESTÁ CADASTRADO.
        return Response({'error': 'Esse usuário já está cadastrado'}, status=status.HTTP_401_UNAUTHORIZED)
      serializer.save()
      return Response({'message': 'Usuário criado'}, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self, request):
    user = User.objects.filter(id=request.user_id).first()
    if (user):
      serializer = UpdateUserSerializer(user, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

  def delete(self, request):
    user = User.objects.filter(id=request.user_id).first()
    if (user):
      user.delete()
      return Response({'message': 'Usuário removido'}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

class UserLoginController(APIView):
  def post(self, request):
    serializer = UserLoginSerializer(data=request.data)

    if serializer.is_valid():
      user = User.objects.filter(email=request.data['email']).first()
      if (user and check_password(request.data['password'], user.password)):
        token = create_user_token(id=user.id)
        return Response({'token': token })
      else:
        return Response({'error': 'Credenciais incorretas'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnimesController(APIView):
  def get(self, request):
    animes = Anime.objects.all()
    serializer = AnimeSerializer(animes, many=True)
    return Response(serializer.data)
  
  def post(self,  request):
    if (request.user_role != 'ADMIN'):
      return Response({'error': 'Você não tem permissão para criar um anime'}, status=status.HTTP_401_UNAUTHORIZED)
    serializer = AnimeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, anime_id):
    if (request.user_role != 'ADMIN'):
      return Response({'error': 'Você não tem permissão para remover um anime'}, status=status.HTTP_401_UNAUTHORIZED)
    anime = Anime.objects.filter(id=anime_id).first()
    if (anime):
      anime.delete()
      return Response({'message': 'Anime removido'}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Anime não encontrado'}, status=status.HTTP_404_NOT_FOUND)

class ListsController(APIView):
  def get(self, request):
    lists = List.objects.filter(user=request.user_id)
    serializer = ListSerializer(lists, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = CreateListSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self, request, id):
    list = List.objects.filter(id=id, user=request.user_id).first()
    if (list):
      list.delete()
      return Response({'message': 'Lista removida'}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Lista não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
  def patch(self, request, id):
    list = List.objects.filter(id=id, user=request.user_id).first()
    if (list):
      serializer = CreateListSerializer(list, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({'error': 'Lista não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
class AnimeCommentsController(APIView):
  def get(self, request, anime_id):
    comments = Comment.objects.filter(anime=anime_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
  
  def post(self, request, anime_id):
    serializer = CreateCommentSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save(anime_id=anime_id)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self, request, comment_id):
    comment = Comment.objects.filter(id=comment_id, author=request.user_id).first()
    if (comment):
      comment.delete()
      return Response({'message': 'Comentário removido'}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Comentário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
