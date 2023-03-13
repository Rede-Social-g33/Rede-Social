from rest_framework import generics
from .models import Comment
from .serializer import CommentsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommentsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        return serializer.save(
            user_id=self.request.user.id, post_id=self.kwargs.get("post_id")
        )


class CommentsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    lookup_url_kwarg = "comment_id"
