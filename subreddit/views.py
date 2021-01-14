from django.shortcuts import render, redirect
from subreddit.models import Subreddit
from subreddit.forms import SubredditCreationForm
from post.models import Post


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
    context = {
        'subreddit': subreddit,
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
    return render(request, 'authentication/generic_form.html', context)
