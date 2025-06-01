from django.contrib import admin
from .models import Post

admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
