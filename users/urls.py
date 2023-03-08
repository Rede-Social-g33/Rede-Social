from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/signup/", ...),  # CRIAR USUARIO
    path("users/<int:user_id>/", ...),  # BUSCAR USUARIO ESPECIFICO
    path("users/<int:friend_id>/friendship", ...),  #
    path("users/<int:friend_id>/follow", ...),  #
    path("users/<int:user_id>/friends", ...),  # LISTAR AMIGOS
    path("users/<int:user_id>/followers", ...),  #
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
