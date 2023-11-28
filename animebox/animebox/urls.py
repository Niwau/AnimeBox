from django.contrib import admin
from django.urls import path
from api.views import UsersController, AnimesController, ListsController, UserLoginController, AnimeCommentsController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account', UsersController.as_view()),
    path('account/<int:user_id>', UsersController.as_view()),
    path('account/login', UserLoginController.as_view()),
    path('animes', AnimesController.as_view()),
    path('animes/<int:anime_id>', AnimesController.as_view()),
    path('animes/<int:anime_id>/comments', AnimeCommentsController.as_view()),
    path('animes/<int:anime_id>/comments/<int:comment_id>', AnimeCommentsController.as_view()),
    path('lists', ListsController.as_view()),
    path('lists/add', ListsController.as_view()), # ENDPOINT PARA ADICIONAR UM ANIME A UMA LISTA
    path('lists/<int:list_id>', ListsController.as_view()),
]