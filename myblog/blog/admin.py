from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('title', 'published_date', 'created_date', 'updated_date')
    list_filter = ('published_date', 'published', 'created_date', 'updated_date')


admin.site.register(Post, PostAdmin)
