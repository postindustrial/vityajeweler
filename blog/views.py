from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Theme
from django.http import Http404
# import ipdb

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def tagged_post_list(request, slug):
    # ipdb.set_trace();
    try:
        theme = Theme.objects.get(slug=slug)
    except Theme.DoesNotExist:
        raise Http404('not found')

    posts = Post.objects.filter(theme=theme).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
