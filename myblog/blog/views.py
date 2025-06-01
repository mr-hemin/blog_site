from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.filter(published=True).order_by('-created_date')
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    next_post = Post.objects.filter(id__gt=post.id, published=True).order_by('id').first()
    previous_post = Post.objects.filter(id__lt=post.id, published=True).order_by('-id').first()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
    })
