from django.forms import ModelForm
from django import forms
from subreddit.models import Subreddit

class SubredditCreationForm(ModelForm):
    class Meta:
        model = Subreddit
        fields = ['title', 'about']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'subreddit_input'}),
        }