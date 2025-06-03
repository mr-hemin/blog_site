from django.urls import path
from .views import index, post_detail, category_posts, about, contact
from django.conf.urls import handler404


urlpatterns = [
    path('', index, name='blog_index'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_posts, name='category_posts'),
    path("/about/", about, name='about'),
    path("/contact/", contact, name='contact'),
]

handler404 = "blog.views.custom_404"
