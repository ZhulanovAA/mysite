from django.conf.urls import url
from .views import posts_list, user_info

urlpatterns = [
    url(r'^$', posts_list, name='posts_list'),
    url(r'^user/(?P<username>[@\+\.\-\w]+)/$', user_info, name='user_info'),
]