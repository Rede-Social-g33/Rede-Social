from django.urls import path
from . import views


urlpatterns = [
    path("likes/<int:likes_id>/", views.LikesDetailsView.as_view()),
]
