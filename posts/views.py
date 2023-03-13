from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from .permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination
from users.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q


class PostListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        self.queryset = self.queryset.filter(
            Q(is_public=True)
            | Q(user=self.request.user)
            | Q(user__friend__user=self.request.user)
            | Q(user__connects__friend=self.request.user)
        )

        return self.queryset


class PostDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    lookup_url_kwarg = "post_id"

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        self.queryset = Post.objects.filter(
            Q(id=post_id, is_public=True)
            | Q(id=post_id, user__friend__user=self.request.user)
        )

        return self.queryset


class UserPostDetailView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    lookup_field = "user_id"

    def get_queryset(self):
        user_obj = get_object_or_404(User, pk=self.kwargs.get("user_id"))

        self.queryset = self.queryset.filter(
            Q(is_public=True, user=user_obj)
            | Q(is_public=False, user=self.request.user)
            | Q(user__friend__user=self.request.user, user=user_obj)
            | Q(user__connects__friend=self.request.user, user=user_obj)
        )

        return self.queryset
