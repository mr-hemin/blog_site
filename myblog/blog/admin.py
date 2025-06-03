from django.contrib import admin
from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('title', 'published_date', 'created_date', 'updated_date')
    list_filter = ('published_date', 'published', 'created_date', 'updated_date')
    search_fields = ("title", "content")


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer_name', 'post', 'text', 'created_date', 'is_approved')
    list_filter = ('is_approved', 'created_date',)
    search_fields = ('writer_name', 'text',)
    actions = ['approve_comment',]
    list_editable = ('is_approved',)

    def approve_comment(self, request, queryset):
        queryset.update(is_approved=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
