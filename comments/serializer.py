from rest_framework import serializers
from .models import Comment


class CommentsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.itens():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Comment
        fields = ["id", "text", "created_at", "post_id", "user_id"]
