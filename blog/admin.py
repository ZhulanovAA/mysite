from django.contrib import admin
from .models import Comment, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_updated', 'author')
    filter_horizontal = ('tags',)
    list_filter = ('author__username', 'tags')
    search_fields = ['title', 'tags__name']
    readonly_fields = ('date_published', 'date_updated')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
