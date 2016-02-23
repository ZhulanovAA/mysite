from django.conf.urls import url
from .views import posts_list

urlpatterns = [
    url(r'^$', posts_list, name='posts-list')
]