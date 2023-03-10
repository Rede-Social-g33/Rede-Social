from django.urls import path
from . import views


urlpatterns = [
    path("comments/<int:comment_id>/", views.CommentsDetailsView.as_view()),
]
