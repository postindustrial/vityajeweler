from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import RealPage, Post, Theme
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
# import ipdb

# Create your views here.

class BaseDetailView(DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.MyObj = get_object_or_404(self.model, slug=self.kwargs['slug'])
        context['seo_title'] = self.MyObj.seo_title
        context['seo_description'] = self.MyObj.seo_description
        context['seo_keywords'] = self.MyObj.seo_keywords
        context['seo_h1'] = self.MyObj.seo_h1
        return context

class BaseListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.MyObj = get_object_or_404(self.model2, slug=self.kwargs['slug'])
        context['seo_title'] = self.MyObj.seo_title
        context['seo_description'] = self.MyObj.seo_description
        context['seo_keywords'] = self.MyObj.seo_keywords
        context['seo_h1'] = self.MyObj.seo_h1
        return context

# вывод списка постов
class PostList(ListView):
    model = Post
    model2 = RealPage
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.model.objects.all()
        self.MyObj = get_object_or_404(self.model2, slug='blog')
        context['seo_title'] = self.MyObj.seo_title
        context['seo_description'] = self.MyObj.seo_description
        context['seo_keywords'] = self.MyObj.seo_keywords
        context['seo_h1'] = self.MyObj.seo_h1
        return context

# вывод постов по тегу
class TaggedList(BaseListView):
    model = Post
    model2 = Theme
    context_object_name = 'posts'
    template = 'post_list.html'

    def get_queryset(self):
        self.MyTheme = get_object_or_404(Theme, slug=self.kwargs['slug'])
        return Post.objects.filter(theme=self.MyTheme)

class PostDetail(BaseDetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



#def tagged_post_list(request, slug):
    # ipdb.set_trace();
#    try:
#        theme = Theme.objects.get(slug=slug)
#    except Theme.DoesNotExist:
#        raise Http404('not found')

#    posts = Post.objects.filter(theme=theme).order_by('-published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})

#def post_detail(request, slug):
#    post = get_object_or_404(Post, slug=slug)
#    return render(request, 'blog/post_detail.html', {'post': post})
