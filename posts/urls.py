from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("posts/", ...),  # CRIAR POSTAGEM, LISTAR POSTAGENS
    path("posts/<int:post_id>/", ...),  #
    path("posts/<int:post_id>/likes", ...),  # CURTIR POST
    path("posts/<int:post_id>/comments", ...),  # COMENTAR POST
    path("posts/<int:user_id>/posts", ...),  # LISTAR POSTAGEM DE USUARIO ESPECIFICO
]
