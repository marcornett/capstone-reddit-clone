from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from post.forms import CreateComment, CreateImagePost, CreateLinkPost, CreateMessagePost
from post.models import Post, PostComment
from post.helper import newPost
from subreddit.helper import random_subreddits, subreddit_search
from subreddit.models import Subreddit

if Subreddit.objects.all():
    search_subreddits = Subreddit.objects.all()


@login_required()
def createPost(request, postType):
    form = None
    subreddit_filter = subreddit_search(request)
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
    context = {
        'form': form,
        'subreddit_filter': subreddit_filter,
        'search_subreddits': search_subreddits
    }
    return render(request, 'post/createpost.html', context)


def postDetail(request, post_id):
    cur_post = Post.objects.get(id=post_id)
    comments = cur_post.comments.all()
    form = CreateComment()
    subreddits = random_subreddits()
    subreddit_filter = subreddit_search(request)
    context = {
        'form': form,
        'post': cur_post,
        'comments': comments,
        'subreddits': subreddits,
        'subreddit_filter': subreddit_filter,
        'search_subreddits': search_subreddits
        }
    return render(request, 'post/postDetail.html', context)


@login_required()
def addComment(request, post_id):
    if request.method == "POST":
        form = CreateComment(request.POST)
        cur_post = Post.objects.get(id=post_id)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = PostComment.objects.create(
                user=request.user,
                message=data['message'],
            )
            cur_post.comments.add(new_comment)
            return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))
    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))


def delete_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    title = post.subreddit.title
    post.delete()
    if request.POST.get('next'):
        next = request.POST.get('next')
        return redirect(next)
    return redirect(f'/subreddit/page/{title}/recent')


@login_required()
def like_dis_post(request, post_id, like_dis):
    cur_post = Post.objects.get(id=post_id)
    if like_dis == "Like":
        cur_post.up_vote.add(request.user)
        cur_post.down_vote.remove(request.user)
    elif like_dis == "Dislike":
        cur_post.down_vote.add(request.user)
        cur_post.up_vote.remove(request.user)

    if request.POST.get('next'):
        next = request.POST.get('next')
        return redirect(next)
    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))


@login_required()
def like_dis_comment(request, comment_id, post_id, like_dis):
    cur_comment = PostComment.objects.get(id=comment_id)
    if like_dis == "Like":
        cur_comment.up_vote.add(request.user)
        cur_comment.down_vote.remove(request.user)
    elif like_dis == "Dislike":
        cur_comment.down_vote.add(request.user)
        cur_comment.up_vote.remove(request.user)

    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post_id}))

