from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='имя')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='автор')
    title = models.CharField(max_length=200, verbose_name='заголовок')
    text = models.TextField('текст')
    date_published = models.DateTimeField('дата публикации')
    date_updated = models.DateTimeField('дата последнего изменения')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='теги')

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_published = now()
        self.date_updated = now()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, models.CASCADE, 'comments')
    author = models.ForeignKey(User, verbose_name='автор')
    text = models.TextField(max_length='500')
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField('дата последнего изменения')
    approved_comment = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.text
