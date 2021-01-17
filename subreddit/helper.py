from subreddit.models import Subreddit
from subreddit.filters import SubredditFilter
import random
subreddits = Subreddit.objects.all()
subreddits_list = list(subreddits)


def random_subreddits():
    random.shuffle(subreddits_list)
    subreddits = subreddits_list[:6]
    return subreddits


def subreddit_search(request):
    subreddit_filter = SubredditFilter(
        request.GET, queryset=subreddits)
    return subreddit_filter
