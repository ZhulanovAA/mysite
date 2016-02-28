from django.conf.urls import url
from .views import posts_list, post_page, user_info

urlpatterns = [
    url(r'^$', posts_list, name='posts_list'),
    url(r'^user/(?P<username>[@\+\.\-\w]+)/$', user_info, name='user_info'),
    url(r'^post/(?P<post_pk>[\d])/$', post_page, name='post_page')
]
