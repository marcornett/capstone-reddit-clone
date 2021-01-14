from django import forms
from reddituser.models import RedditUser


class UpdateUserForm(forms.Form):
    bio = forms.CharField(max_length=250, required=False)
    image = forms.ImageField(required=False)
