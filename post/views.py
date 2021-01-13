from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from django.contrib.auth.decorators import login_required

from post.forms import CreateComment, CreateImagePost, CreateLinkPost, CreateMessagePost
from post.models import Post, PostComment
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
    comments = cur_post.comments.all()
    form = CreateComment()

    return render(request, 'postDetail.html', {'form':form, 'post':cur_post, 'comments': comments})

@login_required()
def addComment(request, post_id):
    if request.method == "POST":
        form = CreateComment(request.POST)
        cur_post = Post.objects.get(id=post_id)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = PostComment.objects.create(
                user = request.user,
                message = data['message'],
            )
            cur_post.comments.add(new_comment)
            HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))

    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))

def subreddit_form(request):
    if request.method == 'POST':
        form = CreateSubreddit(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get("button")
    else:
        form = CreateSubreddit()
    return render(request, 'post/subredditForm.html', locals())
