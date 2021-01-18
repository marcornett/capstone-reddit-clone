from subreddit.models import Subreddit
from subreddit.filters import SubredditFilter
import random


def random_subreddits():
    subreddits = Subreddit.objects.all()
    subreddits_list = list(subreddits)
    random.shuffle(subreddits_list)
    subreddits = subreddits_list[:6]
    return subreddits


def subreddit_search(request):
    subreddits = Subreddit.objects.all()
    subreddit_filter = SubredditFilter(
        request.GET, queryset=subreddits)
    return subreddit_filter
