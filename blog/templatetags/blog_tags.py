from django import template
from django.template.loader import render_to_string

from ..models import Post, Tag


register = template.Library()


@register.simple_tag(takes_context=False)
def tagcloud(selected_tag=None, user=None):
    filters = {}
    if user:
        filters = {'post__author__username': user.username}

    tags = Tag.objects.filter(**filters).distinct()

    context = {
        'observed_user': user,
        'tags': tags,
        'selected_tag': selected_tag,
    }
    return render_to_string('blog/tag_cloud.html', context)
