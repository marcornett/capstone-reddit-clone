from django.db import models
from django.contrib.auth.models import AbstractUser
from subreddit.models import Subreddit

class User(AbstractUser):
    bio = models.TextField(max_length=250)
    #likes = models.IntergerField(default=0)
    #dislikes = models.IntergerField(default=0)
    profile_images = models.ImageField(upload_to='images/')
    subreddit = models.ManyToManyField(Subreddit)