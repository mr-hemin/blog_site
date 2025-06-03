from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('title', 'published_date', 'created_date', 'updated_date')
    list_filter = ('published_date', 'published', 'created_date', 'updated_date')
    search_fields = ("title", "content")


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
