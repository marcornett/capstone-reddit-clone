from django.db import models
from reddituser.models import RedditUser
from subreddit.models import Subreddit
from django.utils import timezone

class PostComment(models.Model):
    user = models.ForeignKey(RedditUser, on_delete=models.CASCADE, related_name="comment_user")
    message = models.CharField(
        max_length=500,
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
    up_vote = models.ManyToManyField(RedditUser, related_name="comment_up_vote")
    down_vote = models.ManyToManyField(RedditUser, related_name="comment_down_vote")
    comments = models.ManyToManyField('self', related_name="comment_comment")

class Post(models.Model):
    user = models.ForeignKey(
        RedditUser, on_delete=models.CASCADE, related_name="user")
    post = models.CharField(
        max_length=500,
        blank=False,
        null=True
    )
    link = models.URLField(
        max_length=200,
        blank=False,
        null=True
    )
    image = models.ImageField(upload_to='images/')
    title = models.CharField(
        max_length=100,
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
    up_vote = models.ManyToManyField(RedditUser, related_name="up_vote")
    down_vote = models.ManyToManyField(RedditUser, related_name="down_vote")
    subreddit = models.ForeignKey(
        Subreddit, on_delete=models.CASCADE
    )
    comments = models.ManyToManyField(PostComment, related_name="post_comment")