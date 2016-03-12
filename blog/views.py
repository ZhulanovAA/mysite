from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Comment, Post


def posts_list(request):
    posts = Post.objects.all()
    if request.GET.get('tag'):
        posts = posts.filter(tags__name=request.GET['tag'])
    context = {'posts': posts}
    return render(request, 'blog/posts_list.html', context)


def user_info(request, username):
    user = get_object_or_404(User, username=username)
    context = {'observed_user': user}
    return render(request, 'blog/user_info.html', context)


def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author__username=user.username)
    if request.GET.get('tag'):
        posts = posts.filter(tags__name=request.GET['tag'])
    context = {'posts': posts, 'observed_user': user}
    return render(request, 'blog/user_posts.html', context)


def post_page(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {'post': post}
    if request.user.has_perm('blog.add_comment'):
        context['form'] = CommentForm()
    return render(request, 'blog/post_page.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        if not request.user.has_perm('blog.add_post'):
            raise PermissionDenied
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_page',
                            post_pk=post.pk)
    else:
        form = PostForm()
    context = {'form': form, 'create': True}
    return render(request, 'blog/form.html', context)


@login_required
def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.author != request.user and not request.user.has_perm('blog.change_post'):
        raise PermissionDenied
    if request.method == 'POST':
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_page',
                            post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'create': False}
    return render(request, 'blog/form.html', context)


@login_required
def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.author != request.user and not request.user.has_perm('blog.delete_post'):
        raise PermissionDenied
    post.delete()
    return redirect('posts_list')


@login_required
def comment_add(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        if not request.user.has_perm('blog.add_comment'):
            raise PermissionDenied
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    return redirect('post_page', post_pk=post_pk)


@login_required
def comment_delete(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.author != request.user and not request.user.has_perm('blog.delete_comment'):
        raise PermissionDenied
    comment.delete()
    return redirect('post_page', post_pk=post_pk)
