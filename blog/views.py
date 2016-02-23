from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/posts_list.html', context)
