from django.db import models
from user.models import RedditUser
from django.utils import timezone


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
    members = models.ManyToManyField(RedditUser)

    def __str__(self):
        return self.title
    