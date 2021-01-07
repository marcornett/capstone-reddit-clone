from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View
from authentication.forms import SignUpForm, LoginForm

class IndexView(View):
    def get(self, request):
        context = {}
        return render(
            request, 'authentication/index.html', context)

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        context = {
            'form': form
        }
        return render(
            request, 'authentication/generic_form.html', context
        )
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO return redirect

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {}
        return render(
            request, 'authentication/generic_form.html', context
        )
    # TODO Post request

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')