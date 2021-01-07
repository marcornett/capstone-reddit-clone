from django.shortcuts import render
from django.views import View

from post.forms import CreateComment, CreateImagePost, CreateLinkPost, CreateMessagePost

def createPost(request, postType):
    form = None

    if postType == 'message':
        form = CreateMessagePost()
    elif postType == 'link':
        form = CreateLinkPost()
    elif postType == 'image':
        form = CreateImagePost()

    return render(request, 'genericForm.html', {'form':form})
