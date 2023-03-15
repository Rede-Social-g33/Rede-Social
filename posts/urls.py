from django.urls import path
from . import views
from likes import views as viewLikes
from comments import views as viewComments


urlpatterns = [
    path("posts/", views.PostListCreateView.as_view()),
    path("posts/<int:post_id>/", views.PostDetailView.as_view()),
    path("posts/<int:post_id>/likes", viewLikes.LikesView.as_view()),
    path("posts/<int:post_id>/comments", viewComments.CommentsView.as_view()),
    path("posts/<int:user_id>/posts", views.UserPostDetailView.as_view()),
]
