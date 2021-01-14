from django.shortcuts import render, redirect
from reddituser.models import RedditUser
from reddituser.forms import UpdateUserForm


def user_profile_view(request, username):
    user = RedditUser.objects.get(username=username)
    form = UpdateUserForm()
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # breakpoint()
            if data['bio']:
                user.bio = data['bio']
            if data['image']:
                user.image = data['image']
            user.save()
            return redirect(f'/user/{username}')
    context = {
        'user': user,
        'form': form
        }
    return render(request, 'reddituser/user_profile.html', context)
