from django.urls import path
from .views import index, post_detail, category_posts


urlpatterns = [
    path('', index, name='blog_index'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_posts, name='category_posts'),
]
