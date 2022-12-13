from django.shortcuts import render, redirect

from .models import Post, Like, Comment
from profiles.models import Profile
from .forms import PostForm, CommentForm


def post_comment(request):
    posts = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    post_form = PostForm()
    comment_form = CommentForm()
    post_add = False

    if 'submit_post_form' in request.POST:
        print(request.POST)
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = profile
            instance.save()
            post_form = PostForm()
            post_add = True

    if 'submit_comment_form' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            comment_form = CommentForm()

    context = {
        'posts': posts,
        'profile': profile,
        'post_form': post_form,
        'comment_form': comment_form,
        'post_add': post_add,
    }
    return render(request, 'posts/main.html', context)


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
        if not created:
            if like.value == 'Лайк':
                like.value = 'Ничего'
            else:
                like.value = 'Лайк'
        else:
            post_obj.save()
            like.save()
    return redirect('posts:post-comment')
