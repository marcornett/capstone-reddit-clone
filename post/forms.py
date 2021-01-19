from django import forms
from subreddit.models import Subreddit


class CreateImagePost(forms.Form):
    title = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'id': 'post_input'}))
    image = forms.ImageField()
    subreddit = forms.ModelChoiceField(queryset=Subreddit.objects.all())


class CreateMessagePost(forms.Form):
    title = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'id': 'post_input'}))
    post = forms.CharField(
        max_length=500,
        widget=forms.Textarea)
    subreddit = forms.ModelChoiceField(queryset=Subreddit.objects.all())


class CreateLinkPost(forms.Form):
    title = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'id': 'post_input'}))
    link = forms.URLField(
        max_length=200)
    subreddit = forms.ModelChoiceField(queryset=Subreddit.objects.all())


class CreateComment(forms.Form):
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'textarea',
                'placeholder': 'Add a comment...'
                }))
