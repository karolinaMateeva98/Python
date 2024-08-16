from django.contrib import admin
from .models import Post, Comment, Hashtag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content', 'hashtags__name']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('author', 'body', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Hashtag)