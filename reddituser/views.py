from django.shortcuts import render, redirect
from reddituser.models import RedditUser
from reddituser.forms import UpdateUserForm
from post.models import Post


def user_profile_view(request, username):
    user = RedditUser.objects.get(username=username)
    form = UpdateUserForm()
    posts = Post.objects.filter(user=request.user)
    sort_by = 'recent'
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
        'sort_by': sort_by
        }
    return render(request, 'reddituser/user_profile.html', context)
