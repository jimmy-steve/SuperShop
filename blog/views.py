from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog_home(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def blog_post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})
