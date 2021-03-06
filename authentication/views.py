from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views import View
from authentication.forms import SignUpForm, LoginForm
from subreddit.models import Subreddit
from django.contrib import messages
from subreddit.helper import random_subreddits, subreddit_search
from post.models import Post

if Subreddit.objects.all():
    search_subreddits = Subreddit.objects.all()


class IndexView(View):
    def get(self, request):
        subreddits = Subreddit.objects.all()
        subreddit_filter = subreddit_search(request)
        subreddits = random_subreddits()
        search_subreddits = Subreddit.objects.all()
        is_home = True
        posts = []
        if request.user.is_authenticated:
            user_subreddits = Subreddit.objects.filter(members=request.user)
            for sub in user_subreddits:
                posts.extend(
                    list(Post.objects.filter(
                        subreddit=sub).order_by(
                            'created_at').reverse()))
        else:
            post_list = list(Post.objects.all())
            post_list = sorted(post_list, key = lambda i: 0 if i.getPopularity() == 0 else -1 / i.getPopularity())
            posts = post_list
        context = {
            'subreddits': subreddits,
            'search_subreddits': search_subreddits,
            'subreddit_filter': subreddit_filter,
            'posts': posts,
            'is_home': is_home
        }
            
        return render(
            request, 'main.html', context)


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        subreddit_filter = subreddit_search(request)
        context = {
            'form': form,
            'subreddit_filter': subreddit_filter,
            'search_subreddits': search_subreddits
        }
        return render(
            request, 'authentication/signupform.html', context
        )

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(
                request, username=username, password=password)
            if user:
                login(request, user)
            return redirect('index')
        context = {'form': form}
        return render(
            request, 'authentication/signupform.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        title = 'Login'
        subreddit_filter = subreddit_search(request)
        context = {
            'form': form, 
            'title': title,
            'subreddit_filter': subreddit_filter,
            'search_subreddits': search_subreddits
            }
        return render(
            request, 'authentication/generic_form.html', context
        )

    def post(self, request):
        form = LoginForm(request.POST)
        title = 'Login'
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username or Password is incorrect.')
                context = {'form': form, 'title': title}
                return render(
                    request, 'authentication/generic_form.html', context)
        context = {'form': form}
        return render(
            request, 'authentication/index.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


def error_500_view(request):
    return render(request, '500.html')


def error_404_view(request, exception):
    return render(request, '404.html')

