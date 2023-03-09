from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination
from users.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication


class PostListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    page_size = 20

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    lookup_url_kwarg = "post_id"


class UserPostDetailView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user_obj = get_object_or_404(User, pk=self.kwargs["user_id"])

        return Post.objects.filter(user_id=user_obj)
