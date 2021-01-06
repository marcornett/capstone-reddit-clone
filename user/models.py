from django.db import models
from django.contrib.auth.models import AbstractUser
from subreddit import Subreddit

class RedditUser(AbstractUser):
    bio = models.TextField(max_length=250)
    likes = models.IntergerField(default=0)
    dislikes = models.IntergerField(default=0)
    images = models.ImageField(upload_to=None)
    subreddit = models.ManyToManyField(Subreddit)
