from django.db import models
from django.contrib.auth.models import AbstractUser


class RedditUser(AbstractUser):
    bio = models.TextField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='images/default_profile.jpg')

    def __str__(self):
        return f'{(self.id)} {self.username}'
    