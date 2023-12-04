from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import List
from api.serializers.list import ListSerializer, CreateListSerializer

class ListController(APIView):
  # RETORNA UMA LISTA ESPECÍFICA.
  def get(self, request, list_id):
    list = List.objects.filter(id=list_id).first()
    if (list):
      serializer = ListSerializer(list, context={'request': request})
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Lista não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
  # DELETA UMA LISTA ESPECÍFICA.
  def delete(self, request, list_id):
    list = List.objects.filter(id=list_id, user=request.user_id).first()
    if (list):
      list.delete()
      return Response({'message': 'Lista removida'}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Lista não encontrada'}, status=status.HTTP_404_NOT_FOUND)
  
  # ATUALIZA O NOME DE UMA LISTA ESPECÍFICA.
  def patch(self, request, list_id):
    list = List.objects.filter(id=list_id, user=request.user_id).first()
    if (list):
      serializer = CreateListSerializer(list, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({'error': 'Lista não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    