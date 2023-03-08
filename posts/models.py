from django.db import models


class Post(models.Model):
    class Meta:
        ordering = ["id"]

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self) -> str:
        return f"<[{self.id}] - Posted by {self.user.username}"
