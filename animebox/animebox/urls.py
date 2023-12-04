from django.contrib import admin
from django.urls import path
from api.views import AccountController, UsersController, AnimesController, AccountController, AnimeController, ListsController, UserLoginController, AnimeCommentsController, ListController
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', UsersController.as_view()),
    path('users/<int:user_id>', UsersController.as_view()),
    path('account', AccountController.as_view()),
    path('account/<int:user_id>', AccountController.as_view()),
    path('account/login', UserLoginController.as_view()),
    path('animes', AnimesController.as_view()),
    path('animes/<int:anime_id>', AnimeController.as_view()),
    path('animes/<int:anime_id>/comments', AnimeCommentsController.as_view()),
    path('animes/<int:anime_id>/comments/<int:comment_id>', AnimeCommentsController.as_view()),
    path('lists', ListsController.as_view()),
    path('lists/add', ListController.as_view()), # ENDPOINT PARA ADICIONAR UM ANIME A UMA LISTA
    path('lists/<int:list_id>', ListController.as_view()),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)