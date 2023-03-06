from django.db import models


class Comment(models.Model):
    class Meta:
        ordering = ["id"]

    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="comments"
    )

    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="comments"
    )
