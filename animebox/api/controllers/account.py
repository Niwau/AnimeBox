from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import User
from api.serializers.account import AccountSerializer, UpdateAccountSerializer, AccountLoginSerializer
from django.contrib.auth.hashers import check_password
from api.utils import create_user_token

class AccountController(APIView):
  # RETORNA A CONTA DO USUÁRIO LOGADO.
  def get(self, request):
    users = User.objects.get(id=request.user_id)
    serializer = AccountSerializer(users)

    if (not users):
      return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    else:
      return Response(serializer.data)

  # CRIA UMA NOVA CONTA COM ROLE=NORMAL.
  def post(self, request):
    data = request.data
    data['role'] = 'NORMAL'
    serializer = AccountSerializer(data=request.data)

    if serializer.is_valid():
      user_exists = User.objects.filter(email=request.data['email']).exists()

      if (user_exists):
        return Response({'error': 'Esse usuário já está cadastrado'}, status=status.HTTP_401_UNAUTHORIZED)
      else:
        serializer.save()
        return Response({'message': 'Usuário criado'}, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  # ATUALIZA O NOME DO USUÁRIO LOGADO.
  def patch(self, request):
    user = User.objects.filter(id=request.user_id).first()

    if (user):
      serializer = UpdateAccountSerializer(user, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

  # DELETA A CONTA DO USUÁRIO LOGADO.
  def delete(self, request):
    user = User.objects.filter(id=request.user_id).first()

    if (user):
      user.delete()
      return Response({'message': 'Usuário removido'}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

# FAZ O LOGIN DO USUÁRIO.
class AccountLoginController(APIView):
  def post(self, request):
    serializer = AccountLoginSerializer(data=request.data)

    if serializer.is_valid():
      user = User.objects.filter(email=request.data['email']).first()
      password_is_valid = check_password(request.data['password'], user.password)

      if (user and password_is_valid):
        token = create_user_token(id=user.id, role=user.role)
        return Response({'token': token, 'id': user.id, 'role': user.role })
      else:
        return Response({'error': 'Credenciais incorretas'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)