from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User
from .models import Connection
from .serializers import ConnectionSerializer, FollowerSerializer, FriendshipSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from rest_framework.exceptions import ValidationError
import ipdb


class FollowView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = [IsAuthenticated]

    lookup_url_kwarg = "friend_id"

    def check_self_follow(self, friend):
        if friend == self.request.user:
            raise ValidationError("You can't follow/unfollow yourself")

    def perform_create(self, serializer):
        friend_id = self.kwargs.get("friend_id")
        friend = get_object_or_404(User, id=friend_id)

        # Verificar se o usuário está tentando seguir a si mesmo
        self.check_self_follow(friend)

        # Verificar se já há uma conexão e atualizar o valor de follow para True caso exista
        connections = Connection.objects.filter(user=self.request.user, friend=friend)

        if connections.exists():
            connection = connections.first()
            if connection.follow:
                raise ValidationError("You already followed him")
            else:
                serializer.instance = connection
                serializer.validated_data["follow"] = True
                self.perform_update(serializer)
        else:
            serializer.save(user=self.request.user, friend=friend, follow=True)

    def destroy(self, request, *args, **kwargs):
        friend = self.get_object()
        self.check_self_follow(friend)

        try:
            connection = Connection.objects.get(user=self.request.user, friend=friend)
        except Connection.DoesNotExist:
            raise ValidationError("You already unfollowed this user")

        instance = connection
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.follow = False
        instance.save()


class FollowerListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(User, id=user_id)
        return Connection.objects.filter(friend=user, follow=True)

class FriendshipCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ConnectionSerializer

    def perform_create(self, serializer):
        user = self.request.user
        friend_id = serializer.validated_data['friend_id']
        status = serializer.validated_data['friendship']


        try:
            friend = User.objects.get(id=friend_id)
        except User.DoesNotExist:
            raise ValidationError('User does not exist')

        connection, created = Connection.objects.get_or_create(user=user, friend=friend, defaults={'friendship': status})

        if not created:
            connection.status = status
            connection.save()
