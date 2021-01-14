from django.core.management.base import BaseCommand, CommandError
from post.models import PostComment
from reddituser.models import RedditUser
import random
from mimesis import Text, Generic
generic = Generic('en')
text = Text()


class Command(BaseCommand):
    help = 'Populates database with users'

    def handle(self, *args, **options):
        for _ in range(2000):
            ids_to_grab = random.randint(1, 1001)
            PostComment.objects.create(
                user=RedditUser.objects.get(id=ids_to_grab),
                message=text.text(),
            )
        self.stdout.write(
                self.style.SUCCESS('Successfully created 2000 comments.')
            )
