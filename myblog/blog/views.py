from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Post, Category
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    query = request.GET.get("q", "")
    posts = Post.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    # 5 posts per page
    paginator = Paginator(posts, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'posts': posts, 'query': query, 'page_obj': page_obj})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    comments = post.comments.order_by("-created_date")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)

    form = CommentForm()

    return render(request, 'blog/detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)

    return render(request, "blog/category_posts.html", {'posts': posts, 'category': category})
