from django.db import models

class Anime(models.Model):
  name=models.CharField(max_length=100)
  sinopsis=models.TextField()
  image=models.ImageField(upload_to='anime')

class User(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField()
  password=models.CharField(max_length=100)
  role=models.CharField(max_length=100)

class Comment(models.Model):
  author=models.ForeignKey(User, on_delete=models.CASCADE)
  anime=models.ForeignKey(Anime, on_delete=models.CASCADE)
  comment=models.TextField()

class List(models.Model):
  name=models.CharField(max_length=100)
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  animes=models.ManyToManyField(Anime)

class Episode(models.Model):
  anime=models.ForeignKey(Anime, on_delete=models.CASCADE)
  title=models.CharField(max_length=100)
