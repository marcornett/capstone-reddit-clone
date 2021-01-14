from django.core.management.base import BaseCommand
from post.models import Post, PostComment
from subreddit.models import Subreddit
from reddituser.models import RedditUser
import urllib
import json
import random
from mimesis import Text, Generic
generic = Generic('en')
text = Text()


class Command(BaseCommand):
    help = 'Populates database with users'

    def handle(self, *args, **options):
        print('Retrieving...')
        for i in range(1, 301):
            ids_to_grab = random.randint(1, 45)
            if i % 6 == 0:
                # image
                with urllib.request.urlopen('https://picsum.photos/v2/list?page={ids_to_grab}&limit=100') as url:
                    data = json.loads(url.read().decode())
                    urllib.request.urlretrieve(
                        data[ids_to_grab]['download_url'], filename=f'media/images/img{i}.jpg')
                post = Post.objects.create(
                    subreddit=Subreddit.objects.get(id=ids_to_grab),
                    user=RedditUser.objects.get(id=i),
                    image=f'images/img{i}.jpg'
                )
                post.comments.add(PostComment.objects.get(id=i))
            elif i % 10 == 0:
                # link
                post = Post.objects.create(
                    subreddit=Subreddit.objects.get(id=ids_to_grab),
                    user=RedditUser.objects.get(id=i),
                    link=generic.internet.home_page(),
                )
                post.comments.add(PostComment.objects.get(id=i))
            else:
                # post
                post = Post.objects.create(
                    subreddit=Subreddit.objects.get(id=ids_to_grab),
                    user=RedditUser.objects.get(id=i),
                    post=f"{text.text()} {''.join(generic.internet.hashtags())}",
                    title=text.title(),
                )
                post.comments.add(PostComment.objects.get(id=i))
        self.stdout.write(
            self.style.SUCCESS('Successfully created 300 posts.')
        )

    # image = models.ImageField(upload_to='images/')
    # up_vote = models.ManyToManyField(RedditUser, related_name="up_vote")
    # down_vote = models.ManyToManyField(RedditUser, related_name="down_vote")
