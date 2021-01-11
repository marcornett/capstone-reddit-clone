from django.db import models
from django.contrib.auth.models import AbstractUser


class RedditUser(AbstractUser):
    bio = models.TextField(max_length=250, null=True, blank=True)
