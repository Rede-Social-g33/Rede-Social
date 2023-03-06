from django.db import models


class Connection(models.Model):
    class Meta:
        ordering = ["id"]

    friendship = models.BooleanField(default=False)
    follow = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="connects"
    )

    friend = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="friend"
    )
