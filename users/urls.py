from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/signup/", ...),
    path("users/<int:user_id>/", ...),
    path("users/<int:friend_id>/friendship", ...),
    path("users/<int:user_id>/friends", ...),
    path("users/<int:user_id>/followers", ...),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
