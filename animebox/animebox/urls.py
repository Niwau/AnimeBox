from django.contrib import admin
from django.urls import path
from api.views import UsersController, AnimesController, ListsController, UserLoginController, AnimeCommentsController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', UsersController.as_view()),
    path('users/login', UserLoginController.as_view()),
    path('animes', AnimesController.as_view()),
    path('animes/<int:anime_id>', AnimesController.as_view()),
    path('animes/<int:anime_id>/comments', AnimeCommentsController.as_view()),
    path('animes/<int:anime_id>/comments/<int:comment_id>', AnimeCommentsController.as_view()),
    path('lists', ListsController.as_view()),
    path('lists/<int:id>', ListsController.as_view()),
]