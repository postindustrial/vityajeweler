from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.ThemeList.as_view()),
]
