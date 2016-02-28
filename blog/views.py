from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    if request.GET.get('tag'):
        posts = posts.filter(tags__name=request.GET['tag'])
    context = {'posts': posts}
    return render(request, 'blog/posts_list.html', context)


def user_info(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author__username=user.username)
    if request.GET.get('tag'):
        posts = posts.filter(tags__name=request.GET['tag'])
    context = {'posts': posts, 'observed_user': user}
    return render(request, 'blog/posts_list.html', context)


def post_page(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {'post': post}
    return render(request, 'blog/post_page.html', context)
