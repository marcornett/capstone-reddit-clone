from django.shortcuts import render
from django.views import View
from subreddit.models import Subreddit
from post.models import Post


def subreddit_view(request, title):
    subreddit = Subreddit.objects.get(title=title)
    posts = Post.objects.filter(subreddit=subreddit)
    members_query = subreddit.members
    members = members_query.all()
    context = {
        'subreddit': subreddit,
        'members': members,
        'posts': posts
        }
    return render(request, 'subreddit/subreddit.html', context)
