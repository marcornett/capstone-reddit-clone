from django.core.management.base import BaseCommand, CommandError
from subreddit.models import Subreddit
from mimesis import Text
text = Text()


class Command(BaseCommand):
    help = 'Populates database with users'

    def handle(self, *args, **options):
        for i in range(30):
            Subreddit.objects.create(
                title=text.word(),
                about=text.text(),
            )
        self.stdout.write(
            self.style.SUCCESS('Successfully created 30 subreddits.')
        )