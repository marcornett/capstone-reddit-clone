from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from post.forms import CreateComment, CreateImagePost, CreateLinkPost, CreateMessagePost
from post.models import Post
from post.helper import newPost

@login_required()
def createPost(request, postType):
    form = None

    if request.method == "POST":
        if postType == 'message':
            form = CreateMessagePost(request.POST)
            newPost(request, form, postType)
        elif postType == 'link':
            form = CreateLinkPost(request.POST)
            newPost(request, form, postType)
        elif postType == 'image':
            form = CreateImagePost(request.POST, request.FILES)
            newPost(request, form, postType)

    if postType == 'message':
        form = CreateMessagePost()
    elif postType == 'link':
        form = CreateLinkPost()
    elif postType == 'image':
        form = CreateImagePost()

    return render(request, 'genericForm.html', {'form':form})

def postDetail(request, post_id):
    cur_post = Post.objects.get(id=post_id)
    form = CreateComment()

    return render(request, 'postDetail.html', {'form':form, 'post':cur_post})
