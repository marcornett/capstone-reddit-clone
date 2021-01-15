from subreddit.models import Subreddit
import random


def random_subreddits():
    subreddits = Subreddit.objects.all()
    subreddits = list(subreddits)
    random.shuffle(subreddits)
    subreddits = subreddits[:6]
    return subreddits
