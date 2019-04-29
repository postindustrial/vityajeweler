from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Page, RealPage, Theme, Place, Company
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
#import ipdb

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

class PlaceList(ListView):
    model = Place
    model2 = RealPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['places'] = self.model.objects.all()
        self.MyObj = get_object_or_404(self.model2, slug='places')
        context['seo_title'] = self.MyObj.seo_title
        context['seo_description'] = self.MyObj.seo_description
        context['seo_keywords'] = self.MyObj.seo_keywords
        context['seo_h1'] = self.MyObj.seo_h1
        return context

class ThemeList(BaseListView):
    model = Place
    model2 = Theme
    context_object_name = 'places'
    template_name = 'place_list.html'

    def get_queryset(self):
        self.MyTheme = get_object_or_404(Theme, slug=self.kwargs['slug'])
        return Place.objects.filter(theme=self.MyTheme)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CompanyList(BaseListView):
    model = Place
    model2 = Company
    context_object_name = 'places'
    template_name = 'place_list.html'

    def get_queryset(self):
        self.MyCompany = get_object_or_404(Company, slug=self.kwargs['slug'])
        return Place.objects.filter(company=self.MyCompany)

class PlaceDetail(BaseDetailView):
    model = Place
    context_object_name = 'place'
