from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'modified_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)