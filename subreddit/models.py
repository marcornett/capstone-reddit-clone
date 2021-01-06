from django.db import models
from user.models import User
class Subreddit(models.Model):
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    about = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        auto_now_add=False
    )
    members = models.ManyToManyField(User)
    