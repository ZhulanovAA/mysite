from django import template
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html_join

from ..models import Post, Tag


register = template.Library()


@register.simple_tag(takes_context=False)
def tagcloud(user=None):
    filters = {}
    if user:
        url = reverse('user_info', username=user.username)
        filters = {'post__author__username': user.username}
    else:
        url = reverse('posts_list')

    tags = Tag.objects.filter(**filters)
    tags = tags.annotate(count=models.Count('post'))
    tags = tags.order_by('name').values_list('name', 'count')
    fmt = '<li><a href="%s?tag={0}">{0} - {1}</a></li>' % url
    return format_html_join('', fmt, tags)
