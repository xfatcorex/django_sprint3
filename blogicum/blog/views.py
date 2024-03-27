from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

POST_QUANTITY = 5

POST = Post.objects.filter(
    category__is_published=True
)


def post_filter(posts_manager):
    return posts_manager.filter(
        pub_date__date__lte=timezone.now(),
        is_published=True
    )


def index(request):
    template = 'blog/index.html'
    post_list = post_filter(POST)[:POST_QUANTITY]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(post_filter(POST), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = post_filter(category.posts)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
