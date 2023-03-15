from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(
        unique=True, error_messages={"unique": "This field must be unique."}
    )
    updated_at = models.DateTimeField(auto_now=True)
