from django.contrib import admin
from django import forms

from .models import Post, Category


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['category_title',
                                         'category_description']}),
    ]
    inlines = [PostInline]
    list_display = ('category_title', 'category_description')
    search_fields = ['category_title']


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'pub_date', 'likes', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['post_title', 'post_text']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
