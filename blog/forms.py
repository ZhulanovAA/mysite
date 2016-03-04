from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('date_published', 'date_updated', 'author')
