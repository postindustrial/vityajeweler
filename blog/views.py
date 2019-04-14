from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Theme

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})