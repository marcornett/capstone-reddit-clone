from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from subreddit.models import Subreddit
from subreddit.forms import SubredditCreationForm
from subreddit.filters import SubredditFilter
from post.models import Post
from subreddit.helper import random_subreddits
import random


def subreddit_view(request, title, sort_by):
    subreddit = Subreddit.objects.get(title=title)
    posts = list()
    if sort_by == 'trending':
        post_list = list(Post.objects.all())
        post_list.sort(key=lambda x: x.up_vote.count() - x.down_vote.count())
        posts = post_list[::-1]
    else:
        posts = Post.objects.filter(subreddit=subreddit).order_by('created_at').reverse()
    members_query = subreddit.members
    members = members_query.all()
    subreddits = random_subreddits()
    context = {
        'subreddit': subreddit,
        'subreddits': subreddits,
        'members': members,
        'posts': posts,
        'sort_by': sort_by,
        }
    return render(request, 'subreddit/subreddit.html', context)


def subreddit_creation_view(request):
    form = SubredditCreationForm()
    title = 'Create Subreddit'
    if request.method == "POST":
        form = SubredditCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Subreddit.objects.create(
                title=data['title'],
                about=data['about']
            )
            return redirect(f"/subreddit/page/{data['title']}/recent")
    context = {'form': form, 'title': title}
    return render(request, 'subreddit/createsubreddit.html', context)


def subreddit_search_view(request):
    subreddits = Subreddit.objects.all()
    subreddit_filter = SubredditFilter(request.GET, queryset=subreddits)
    subreddits = subreddit_filter.qs[:6]
    posts = []
    for subreddit in subreddits:
        query_set = Post.objects.filter(subreddit=subreddit)
        for post in query_set:
            posts.append(post)
    random.shuffle(posts)
    context = {
        'subreddits': subreddits,
        'subreddit_filter': subreddit_filter,
        'posts': posts
        }
    return render(request, 'subreddit/search.html', context)
