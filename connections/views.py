from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User
from .models import Connection
from .serializers import ConnectionSerializer
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
