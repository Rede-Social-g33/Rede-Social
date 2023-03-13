from django.db import models


class Connection(models.Model):
    class Meta:
        ordering = ["id"]
    
    STATUS_CHOICES = (
        ('connected', 'Connected'),
        ('not_connected', 'Not Connected'),
        ('pending', 'Pending'),
    )

    friendship = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_connected')
    follow = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="connects"
    )

    friend = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="friend"
    )
