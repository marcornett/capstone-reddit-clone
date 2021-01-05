from django.db import models
from user import User
from subreddit import Subreddit
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.Charfield(
        max_length=500,
        blank=False,
        null=True
    )
    link = models.URLField(
        max_length=200,
        blank=False,
        null=True
    )
    title = models.CharField(
        max_length=50,
        blank=False,
        null=True
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        auto_now_add=False
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        auto_now_add=False
    )
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    subreddit = models.ForeignKey(
        Subreddit, on_delete=models.CASCADE
    )