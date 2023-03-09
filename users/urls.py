from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/signup/", views.UserView.as_view()),  # CRIAR USUARIO
    path(
        "users/<int:user_id>/", views.UserDetailView.as_view()
    ),  # BUSCAR USUARIO ESPECIFICO, EDITAR, DELETAR
    path("users/<int:friend_id>/friendship", ...),  #
    path("users/<int:friend_id>/follow", ...),  #
    path("users/<int:user_id>/friends", ...),  # LISTAR AMIGOS
    path("users/<int:user_id>/followers", ...),  #
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
