from django.core.management.base import BaseCommand, CommandError
from reddituser.models import RedditUser
from mimesis import Person
person = Person('en')


class Command(BaseCommand):
    help = 'Populates database with users'

    def handle(self, *args, **options):
        is_active = False
        for i in range(30):
            if i % 3 == 0:
                is_active = True
            RedditUser.objects.create(
                password=person.password(),
                username=person.username(),
                email=person.email(),
                is_active=is_active,
                first_name=person.first_name(),
                last_name=person.last_name(),
                bio=person.occupation()
            )
            is_active = False
        self.stdout.write(self.style.SUCCESS('Successfully created 30 users.'))
