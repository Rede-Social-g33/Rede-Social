from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Like.objects.create(**validated_data)

    class Meta:
        model = Like
        fields = ["id", "created_at", "post_id", "user_id"]
