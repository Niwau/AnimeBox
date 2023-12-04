from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import User
from api.serializers.users import UserSerializer
from api.serializers.account import AccountSerializer

class UsersController(APIView):
  # RETORNA TODOS OS USUÁRIOS DO SISTEMA.
  def get(self, request):
    if (request.user_role == 'ADMIN'):
      users = User.objects.all()
      serialier = UserSerializer(users, many=True)
      return Response(serialier.data)
    else:
      return Response({'error': 'Você não possui permissão'})
  
  # DELETA UM USUÁRIO DO SISTEMA.
  def delete(self, request, user_id):
    if (request.user_role == 'ADMIN'):
      user = User.objects.filter(id=user_id).first()

      if (user):
        user.delete()
        return Response({'message': 'Usuário removido'}, status=status.HTTP_200_OK)
      else:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND) 
    else:
      return Response({'error': 'Você não possui permissão'})

  # CRIA UM USÁRIO ADMINISTRADOR.
  def post(self, request):
    if (request.user_role == 'ADMIN'):
      data = request.data
      data['role'] = 'ADMIN'
      serializer = AccountSerializer(data=data)

      if serializer.is_valid():
        user_exists = User.objects.filter(email=request.data['email']).exists()

        if (user_exists):
          return Response({'error': 'Esse usuário já está cadastrado'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
          serializer.save()
          return Response({'message': 'Usuário criado'}, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({'error': 'Você não possui permissão'})