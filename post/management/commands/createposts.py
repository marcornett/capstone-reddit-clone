from django.core.management.base import BaseCommand, CommandError
from post.models import Post, PostComment
from subreddit.models import Subreddit
from reddituser.models import RedditUser
from mimesis import Text, Generic
generic = Generic('en')
text = Text()


class Command(BaseCommand):
    help = 'Populates database with users'

    def handle(self, *args, **options):
        for i in range(10):
            if i % 6 == 0:
                # image
                Post.objects.create(
                    subreddit=Subreddit.objects.get(id=i),
                    user=RedditUser.objects.get(id=i),
                    comments=PostComment.objects.get(id=i),
                    # image ?
                )
            elif i % 10 == 0:
                # link
                Post.objects.create(
                    subreddit=Subreddit.objects.get(id=i),
                    user=RedditUser.objects.get(id=i),
                    comments=PostComment.objects.get(id=i),
                    link=generic.internet.home_page(),
                )
            else:
                # post
                Post.objects.create(
                    subreddit=Subreddit.objects.get(id=i),
                    user=RedditUser.objects.get(id=i),
                    comments=PostComment.objects.get(id=i),
                    post=f"{text.text()} {''.join(generic.internet.hashtags())}",
                    title=text.title(),
                )
        self.stdout.write(
            self.style.SUCCESS('Successfully created 10 subreddits.')
        )

    # image = models.ImageField(upload_to='images/')
    # up_vote = models.ManyToManyField(RedditUser, related_name="up_vote")
    # down_vote = models.ManyToManyField(RedditUser, related_name="down_vote")
