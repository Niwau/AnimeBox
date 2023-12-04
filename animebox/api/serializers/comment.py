from rest_framework import serializers
from api.models import Comment

class CommentSerializer(serializers.ModelSerializer):
  author = serializers.SerializerMethodField()
  author_id = serializers.SerializerMethodField()

  def get_author(self, obj):
    return obj.author.name

  def get_author_id(self, obj):
    return obj.author.id

  class Meta:
    model = Comment
    fields = ['author', 'comment', 'id', 'author_id']

class CreateCommentSerializer(serializers.ModelSerializer):
  def create(self, validated_data):
    user_id = self.context['request'].user_id
    comment = Comment.objects.create(author_id=user_id, **validated_data)
    return comment

  class Meta:
    model = Comment
    fields = ['comment']
