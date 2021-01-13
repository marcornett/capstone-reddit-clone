from django.forms import ModelForm
from subreddit.models import Subreddit

class SubredditCreationForm(ModelForm):
    class Meta:
        model = Subreddit
        fields = ['title', 'about']