from rest_framework import serializers
from .models import Connection


class ConnectionSerializer(serializers.ModelSerializer):
    friend = serializers.StringRelatedField()

    class Meta:
        model = Connection
        fields = ["id", "friend", "friendship", "follow", "created_at"]
        read_only_fields = ["id", "friend", "friendship", "follow", "created_at"]

    # def update(self, instance, validated_data):
    #     instance.follow = validated_data.get("follow", instance.follow)
    #     instance.save()
    #     return instance
