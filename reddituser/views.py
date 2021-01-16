from django.shortcuts import render, redirect
from reddituser.models import RedditUser
from reddituser.forms import UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from post.models import Post
from subreddit.models import Subreddit


def user_profile_view(request, username):
    user = RedditUser.objects.get(username=username)
    form = UpdateUserForm()
    posts = Post.objects.filter(
        user=request.user).order_by("created_at").reverse()
    sort_by = 'recent'
    joined = Subreddit.objects.filter(members=request.user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data['bio']:
                user.bio = data['bio']
            if data['image']:
                user.image = data['image']
            user.save()
            return redirect(f'/user/{username}')
    context = {
        'user': user,
        'form': form,
        'posts': posts,
        'sort_by': sort_by,
        'joined': joined
        }
    return render(request, 'reddituser/user_profile.html', context)

@login_required()
def delete_profile_view(request, username):
    if request.method == "POST":
        user = RedditUser.objects.get(username=username)
        if request.user == user:
            logout(request)
        user.delete()

        return redirect('/')

    return render(request, 'reddituser/delete_check.html', {'username':username})
