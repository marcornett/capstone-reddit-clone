from django import forms
from django.contrib.auth.forms import UserCreationForm
from reddituser.models import RedditUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = RedditUser
        fields = UserCreationForm.Meta.fields + ('email', 'bio')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
