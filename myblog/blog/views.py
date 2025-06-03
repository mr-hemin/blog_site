from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q


def index(request):
    query = request.GET.get("q", "")
    posts = Post.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    return render(request, 'blog/index.html', {'posts': posts, 'query': query})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    next_post = Post.objects.filter(id__gt=post.id, published=True).order_by('id').first()
    previous_post = Post.objects.filter(id__lt=post.id, published=True).order_by('-id').first()

    return render(request, 'blog/detail.html', {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
    })


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)

    return render(request, "blog/category_posts.html", {'posts': posts, 'category': category})
