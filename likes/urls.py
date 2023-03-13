from django.urls import path
from . import views


urlpatterns = [
    path("likes/<int:like_id>/", views.LikesDetailsView.as_view()),
]
