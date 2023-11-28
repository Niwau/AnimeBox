from rest_framework import serializers
from api.models import Anime, User, Comment, List, Episode
from django.contrib.auth import hashers

class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ['name', 'sinopsis', 'image', 'id']

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = hashers.make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        return user

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role', 'id']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'role', 'id']

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.name

    class Meta:
        model = Comment
        fields = ['author', 'comment', 'id']

class CreateCommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user_id = self.context['request'].user_id
        comment = Comment.objects.create(author_id=user_id, **validated_data)
        return comment

    class Meta:
        model = Comment
        fields = ['comment']

class ListSerializer(serializers.ModelSerializer):
    animes = AnimeSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ['name', 'animes', 'id']

class CreateListSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user_id = self.context['request'].user_id
        list = List.objects.create(user_id=user_id, **validated_data)
        return list

    class Meta:
        model = List
        fields = ['name']

class PushAnimeToListSerializer(serializers.Serializer):
    anime_id = serializers.IntegerField()
    list_id = serializers.IntegerField()

    def validate(self, data):
        if not data.get('list_id') or not data.get('anime_id'):
            raise serializers.ValidationError("list_id ou anime_id inválido")
        return data

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ['anime', 'title', 'id']