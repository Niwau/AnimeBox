from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import List
from api.serializers.list import ListSerializer, CreateListSerializer

class ListsController(APIView):
  # RETORNA TODAS AS LISTAS DO USUÁRIO.
  def get(self, request):
    lists = List.objects.filter(user=request.user_id)
    serializer = ListSerializer(lists, many=True, context={'request': request})
    return Response(serializer.data)
  
  # CRIA UMA NOVA LISTA.
  def post(self, request):
    serializer = CreateListSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
