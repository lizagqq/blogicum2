from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import Post, Category

def index(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (post.pub_date > timezone.now() or 
        not post.is_published or 
        not post.category.is_published):
        raise Http404
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug, is_published=True)
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {'category': category, 'post_list': posts})

def about(request):
    return render(request, 'blog/about.html')

def rules(request):
    return render(request, 'blog/rules.html')