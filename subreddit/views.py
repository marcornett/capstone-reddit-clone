from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from subreddit.models import Subreddit
from subreddit.forms import SubredditCreationForm
from reddituser.models import RedditUser
from post.models import Post
from subreddit.helper import random_subreddits, subreddit_search
import random

if Subreddit.objects.all():
    search_subreddits = Subreddit.objects.all()

def subreddit_view(request, title, sort_by):
    subreddit = Subreddit.objects.get(title=title)
    subreddits = random_subreddits()
    members_query = subreddit.members
    members = members_query.all()
    subreddit_filter = subreddit_search(request)
    is_member = request.user in subreddit.members.all()
    posts = list()

    if sort_by == 'trending':
        current_subreddit = Subreddit.objects.filter(title=title).first()
        post_list = list(Post.objects.filter(subreddit=current_subreddit))
        post_list = sorted(post_list, key = lambda i: 0 if i.getPopularity() == 0 else -1 / i.getPopularity())
        posts = post_list
    else:
        posts = Post.objects.filter(subreddit=subreddit).order_by('created_at').reverse()

    context = {
        'subreddit': subreddit,
        'subreddits': subreddits,
        'members': members,
        'posts': posts,
        'sort_by': sort_by,
        'is_member': is_member,
        'subreddit_filter': subreddit_filter,
        'search_subreddits': search_subreddits
        }

    return render(request, 'subreddit/subreddit.html', context)


def subreddit_creation_view(request):
    form = SubredditCreationForm()
    title = 'Create Subreddit'
    subreddit_filter = subreddit_search(request)
    if request.method == "POST":
        form = SubredditCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Subreddit.objects.create(
                title=data['title'],
                about=data['about']
            )
            return redirect(f"/subreddit/page/{data['title']}/recent")
    context = {
        'form': form, 
        'title': title,
        'subreddit_filter': subreddit_filter,
        'search_subreddits': search_subreddits
        }
    return render(request, 'subreddit/createsubreddit.html', context)


def subreddit_search_view(request):
    subreddits = Subreddit.objects.all()
    subreddit_filter = subreddit_search(request)
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
        'posts': posts,
        'search_subreddits': search_subreddits
        }
    return render(request, 'subreddit/search.html', context)


def subscribe(request, subreddit_id):
    current_subreddit = Subreddit.objects.get(id=subreddit_id)
    if request.user in current_subreddit.members.all():
        current_subreddit.members.remove(request.user)
    else:
        current_subreddit.members.add(request.user)
    last_url_list = request.META.get('HTTP_REFERER').split('/')
    last_url_list = list(filter(None, last_url_list))
    return HttpResponseRedirect(
        reverse('subreddit', kwargs={
            'title': current_subreddit.title,
            'sort_by': last_url_list[-1]
            }))

