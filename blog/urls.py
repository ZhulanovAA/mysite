from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', posts_list, name='posts_list'),
    url(r'^user/(?P<username>[@\+\.\-\w]+)/$',
        user_info, name='user_info'),
    url(r'^post/(?P<post_pk>[\d])/$',
        post_page, name='post_page'),
    url(r'^post/create/$', post_create,
        name='post_create'),
    url(r'^post/(?P<post_pk>\d+)/edit/$', post_edit,
        name='post_edit'),
]
