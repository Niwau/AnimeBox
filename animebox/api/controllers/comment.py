from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import Comment
from api.serializers.comment import CommentSerializer, CreateCommentSerializer

class CommentController(APIView):
  # RETORNA TODOS OS COMENTÁRIOS DO ANIME.
  def get(self, request, anime_id):
    comments = Comment.objects.filter(anime=anime_id).order_by('-id')
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
  
  # CRIA UM NOVO COMENTÁRIO NO ANIME.
  def post(self, request, anime_id):
    serializer = CreateCommentSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save(anime_id=anime_id)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  # DELETA UM COMENTÁRIO DO ANIME.
  def delete(self, request, anime_id, comment_id):
    comment = Comment.objects.filter(id=comment_id, author=request.user_id).first()
    if (comment):
      comment.delete()
      return Response({'message': 'Comentário removido'}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Comentário não encontrado'}, status=status.HTTP_404_NOT_FOUND)