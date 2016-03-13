from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', posts_list, name='posts_list'),
    url(r'^user/(?P<username>[@\+\.\-\w]+)/$',
        user_info, name='user_info'),
    url(r'^user/(?P<username>[@\+\.\-\w]+)/posts/$',
        user_posts, name='blog_user_posts'),
    url(r'^post/(?P<post_pk>[\d]+)/$',
        post_page, name='post_page'),
    url(r'^post/create/$', post_create,
        name='post_create'),
    url(r'^post/(?P<post_pk>[\d]+)/edit/$', post_edit,
        name='post_edit'),
    url(r'^post/(?P<post_pk>[\d]+)/delete/$', post_delete,
        name='post_delete'),
    url(r'^post/(?P<post_pk>[\d]+)/add_comment/$', comment_add,
        name='blog_comment_add'),
    url(r'^post/(?P<post_pk>[\d]+)/comment(?P<comment_pk>[\d]+)/delete$', comment_delete,
        name='blog_comment_delete'),
]
