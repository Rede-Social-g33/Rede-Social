from rest_framework import serializers
from .models import Connection


class ConnectionSerializer(serializers.ModelSerializer):
    friend = serializers.StringRelatedField()

    class Meta:
        model = Connection
        fields = ["id", "friend", "friendship", "follow", "created_at"]
        read_only_fields = ["id", "friend", "friendship", "follow", "created_at"]


class FollowerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_user_id(self, obj):
        return obj.user.id

    class Meta:
        model = Connection
        fields = ("id", "username", "user_id")
