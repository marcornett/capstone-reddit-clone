from post.models import Post

def newPost(request, form, postType):
    new_post = None
    if form.is_valid():
        data = form.cleaned_data
        if postType == 'message':
            new_post = Post.objects.create(
                user = request.user,
                subreddit = data['subreddit'],
                post = data['post'],
                title = data['title'],
            )
        elif postType == 'link':
            new_post = Post.objects.create(
                user = request.user,
                subreddit = data['subreddit'],
                link = data['link'],
                title = data['title'],
            )
        elif postType == 'image':
            print('creating image')
            new_post = Post.objects.create(
                user = request.user,
                subreddit = data['subreddit'],
                image = data['image'],
                title = data['title'],
            )
    else:
        print("form wasn't valid")

    return new_post
