from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views import View
from authentication.forms import SignUpForm, LoginForm
from reddituser.models import RedditUser
from subreddit.models import Subreddit

class IndexView(View):
    def get(self, request):
        subreddits = Subreddit.objects.all()
        context = {
            'subreddits': subreddits
        }
        return render(
            request, 'authentication/index.html', context)

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        context = {
            'form': form
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
        context = {'form': form}
        return render(
            request, 'authentication/generic_form.html', context
        )

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request, username=username, password=password)
            if user:
                login(request, user)
            return redirect('index')
        context = {'form': form}
        return render(
            request, 'authentication/index.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')