from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("posts/", views.PostListCreateView.as_view()),
    path("posts/<int:post_id>/", views.PostDetailView.as_view()),
    path("posts/<int:post_id>/likes", ...),
    path("posts/<int:post_id>/comments", ...),
    path("posts/<int:user_id>/posts", ...),
]
