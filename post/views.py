from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from post.forms import CreateComment, CreateImagePost, CreateLinkPost, CreateMessagePost
from post.models import Post, PostComment
from post.helper import newPost

@login_required()
def createPost(request, postType):
    form = None

    if request.method == "POST":
        cur_post = None
        if postType == 'message':
            form = CreateMessagePost(request.POST)
            cur_post = newPost(request, form, postType)
        elif postType == 'link':
            form = CreateLinkPost(request.POST)
            cur_post = newPost(request, form, postType)
        elif postType == 'image':
            form = CreateImagePost(request.POST, request.FILES)
            cur_post = newPost(request, form, postType)
        if cur_post:
            return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':cur_post.id}))

    if postType == 'message':
        form = CreateMessagePost()
    elif postType == 'link':
        form = CreateLinkPost()
    elif postType == 'image':
        form = CreateImagePost()
    return render(request, 'post/createpost.html', {'form':form})

  
def postDetail(request, post_id):
    cur_post = Post.objects.get(id=post_id)
    comments = cur_post.comments.all()
    form = CreateComment()

    return render(request, 'post/postDetail.html', {'form':form, 'post':cur_post, 'comments': comments})

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
            return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))

    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))


def delete_post_view(request, post_id, sort_by):
    title = {}
    post = Post.objects.get(id=post_id)
    title['title'] = post.subreddit.title
    post.delete()
    return redirect(f"/subreddit/page/{title['title']}/{sort_by}")


@login_required()
def dislike_post(request, post_id):
    cur_post = Post.objects.get(id=post_id)

    cur_post.down_vote.add(request.user)
    cur_post.up_vote.remove(request.user)

    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))

@login_required()
def like_post(request, post_id):
    cur_post = Post.objects.get(id=post_id)

    cur_post.up_vote.add(request.user)
    cur_post.down_vote.remove(request.user)

    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))

@login_required()
def dislike_comment(request, comment_id, post_id):
    cur_comment = PostComment.objects.get(id=comment_id)

    cur_comment.down_vote.add(request.user)
    cur_comment.up_vote.remove(request.user)

    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))

@login_required()
def like_comment(request, comment_id, post_id):
    cur_comment = PostComment.objects.get(id=comment_id)

    cur_comment.up_vote.add(request.user)
    cur_comment.down_vote.remove(request.user)

    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))
