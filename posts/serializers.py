from rest_framework import serializers
from .models import Post
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "text",
            "created_at",
            "updated_at",
            "is_public",
            "posted_by",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "posted_by"]

    posted_by = serializers.SerializerMethodField()

    def get_posted_by(self, obj):
        return {"username": obj.user.username, "id": obj.user.id}
