from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/posts_list.html', context)


def user_info(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author__username=user.username)
    context = {'posts': posts, 'observed_user': user}
    return render(request, 'blog/posts_list.html', context)
