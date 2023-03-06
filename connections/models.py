from django.db import models


class Connection(models.Model):
    class Meta:
        ordering = ["id"]

    friendship = models.BooleanField(default=False)
    follow = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_id"
    )

    friend = models.ForeignKey(
        "users.user", on_delete=models.CASCADE, related_name="friend_id"
    )
