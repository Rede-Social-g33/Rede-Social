from rest_framework import generics
from .models import Like
from .serializer import LikeSerializer


class LikesView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        return serializer.save(
            user_id=self.request.user.id, post_id=self.kwargs.get("post_id")
        )
