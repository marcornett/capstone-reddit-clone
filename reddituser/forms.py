from django import forms
from reddituser.models import RedditUser


class UpdateUserForm(forms.Form):
    bio = forms.CharField(
        max_length=250, 
        required=False, 
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Bio'
                })
        )
    image = forms.ImageField(
        required=False,
        # widget=forms.ImageField(
        #     attrs={
        #         'class': 'file-input',
        #         'placeholder': 'Bio'
        #         })
        )
