from django.shortcuts import get_object_or_404, get_list_or_404, render

from django.utils import timezone

from .models import Category, Post

POST_QUANTITY = 5

POST = Post.objects.filter(
        is_published=True,
        category__is_published=True
)

def post_filter(model):
    time_now = model.filter(pub_date__date__lte=timezone.now())
    return time_now

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
    post_list = get_list_or_404(
        post_filter(category.posts),
        is_published=True
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
