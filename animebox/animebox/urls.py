from django.contrib import admin
from django.urls import path
from api.views import UsersController, AnimesController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', UsersController.as_view()),
    path('anime', AnimesController.as_view())
]
