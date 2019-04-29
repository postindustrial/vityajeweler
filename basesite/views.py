from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import RealPage, Banner
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView, View
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

class MainPage(ListView):
    model = RealPage
    model2 = Banner
    template = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.MyObj = get_object_or_404(self.model, slug='main')
        context['seo_title'] = self.MyObj.seo_title
        context['seo_description'] = self.MyObj.seo_description
        context['seo_keywords'] = self.MyObj.seo_keywords
        context['seo_h1'] = self.MyObj.seo_h1
        context['content'] = self.MyObj.content
        context['body_bottom_banners'] = Banner.objects.filter(place="body_bottom")
        return context
