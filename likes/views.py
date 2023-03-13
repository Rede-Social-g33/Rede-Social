from rest_framework import generics

from likes.permissions import IsLikeOwner
from .models import Like
from .serializer import LikeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class LikesView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        return serializer.save(
            user_id=self.request.user.id, post_id=self.kwargs.get("post_id")
        )


class LikesDetailsView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsLikeOwner]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_url_kwarg = "like_id"
