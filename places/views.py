from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Theme, Place, Company
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
#import ipdb

# Create your views here.


# вывод списка постов
class PlaceList(ListView):
    model = Place

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['places'] = Place.objects.all()
        return context

class ThemeList(ListView):
    model = Place
    context_object_name = 'places'
    template_name = 'place_list.html'

    def get_queryset(self):
        self.MyTheme = get_object_or_404(Theme, slug=self.kwargs['slug'])
        return Place.objects.filter(theme=self.MyTheme)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CompanyList(ListView):
    model = Place
    context_object_name = 'places'
    template_name = 'place_list.html'

    def get_queryset(self):
        self.MyCompany = get_object_or_404(Company, slug=self.kwargs['slug'])
        return Place.objects.filter(company=self.MyCompany)

class PlaceDetail(DetailView):
    model = Place
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
