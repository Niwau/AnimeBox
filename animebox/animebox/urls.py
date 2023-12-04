from django.contrib import admin
from django.urls import path
from api.controllers import account, anime, anime_list, animes, comment, list, lists, users
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account', account.AccountController.as_view()),
    path('account/login', account.AccountLoginController.as_view()),
    path('users', users.UsersController.as_view()),
    path('users/<int:user_id>', users.UsersController.as_view()),
    path('animes', animes.AnimesController.as_view()),
    path('animes/<int:anime_id>', anime.AnimeController.as_view()),
    path('animes/<int:anime_id>/comments', comment.CommentController.as_view()),
    path('animes/<int:anime_id>/comments/<int:comment_id>', comment.CommentController.as_view()),
    path('lists', lists.ListsController.as_view()),
    path('lists/add', anime_list.AnimeListController.as_view()),
    path('lists/<int:list_id>', list.ListController.as_view()),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)