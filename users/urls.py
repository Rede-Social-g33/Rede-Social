from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from connections.views import FollowView, FollowerListView

urlpatterns = [
    path("users/signup/", views.UserView.as_view()),
    path("users/<int:user_id>/", views.UserDetailView.as_view()),
    # path("users/<int:friend_id>/friendship", ...),  #
    path("users/<int:friend_id>/follow", FollowView.as_view()),  #
    # path("users/<int:user_id>/friends", ...),  # LISTAR AMIGOS
    path("users/<int:user_id>/followers", FollowerListView.as_view()),  #
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
