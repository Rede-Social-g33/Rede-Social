from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from connections.permissions import IsConnectionsOwner
from users.models import User
from .models import Connection
from .serializers import ConnectionSerializer, FollowerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from rest_framework.exceptions import ValidationError
from django.db.models import Q


class FollowView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = [IsAuthenticated, IsConnectionsOwner]

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
        connections = Connection.objects.filter(
            sender=self.request.user, receiver=friend
        )

        if connections.exists():
            connection = connections.first()
            if connection.follow:
                raise ValidationError("You already followed him")
            else:
                serializer.instance = connection
                serializer.validated_data["follow"] = True
                self.perform_update(serializer)
        else:
            serializer.save(sender=self.request.user, receiver=friend, follow=True)

    def destroy(self, request, *args, **kwargs):
        friend = self.get_object()
        self.check_self_follow(friend)

        try:
            connection = Connection.objects.get(
                sender=self.request.user, receiver=friend
            )
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
        user_id = self.request.user.id
        user = get_object_or_404(User, id=user_id)
        return Connection.objects.filter(receiver=user, follow=True)


class FriendshipView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ConnectionSerializer
    lookup_field = "friend_id"
    queryset = Connection.objects.all()

    def perform_create(self, serializer):
        friend_id = self.kwargs.get("friend_id")
        friend = get_object_or_404(User, id=friend_id)

        if friend == self.request.user:
            raise ValidationError("you can't follow yourself")

        connections = Connection.objects.filter(
            Q(sender=self.request.user, receiver=friend, follow=True)
            | Q(sender=friend, receiver=self.request.user, follow=True)
        ).first()

        if connections:
            if connections.friendship == "connected" or "pending":
                raise ValidationError("You already connected him")
        else:
            serializer.save(
                sender=self.request.user,
                receiver=friend,
                follow=True,
                friendship="pending",
            )

    def get_queryset(self):
        list_connections = Connection.objects.filter(
            Q(sender_id=self.request.user.id, friendship="connected")
            | Q(receiver_id=self.request.user.id, friendship="connected")
        )

        return list_connections


class FriendshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ConnectionSerializer
    lookup_url_kwarg = "connection_id"
    queryset = Connection.objects.all()

    def perform_update(self, serializer):
        connection_id = self.kwargs.get("connection_id")
        conection = get_object_or_404(Connection, pk=connection_id)

        print(conection.user_id)

        if conection:
            if conection.friendship == "connected":
                raise ValidationError("You already connected him")
            elif conection.user_id == self.request.user.id:
                if conection.friendship == "pending":
                    raise ValidationError("You already peding him")
                elif conection.friendship == "not_connected":
                    print("loop+not_conect")
                    serializer.instance = conection
                    serializer.validated_data["friendship"] = "pending"
                    serializer.save()

                    return serializer

            elif conection.friendship == "pending":
                serializer.save(friendship="connected")
