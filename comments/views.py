from rest_framework import generics
from .models import Comment
from .serializer import CommentsSerializer


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        return serializer.save(
            user_id=self.request.user.id, post_id=self.kwargs.get("post_id")
        )
