from django import forms

class CreateImagePost(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()

class CreateMessagePost(forms.Form):
    title = forms.CharField(max_length=50)
    post = forms.CharField(max_length=500, widget=forms.Textarea)

class CreateLinkPost(forms.Form):
    title = forms.CharField(max_length=50)
    link = forms.URLField(max_length=200)

class CreateComment(forms.Form):
    pass