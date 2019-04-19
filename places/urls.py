from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.PlaceList.as_view()),
    path('theme/<slug:slug>/', views.ThemeList.as_view()),
    path('company/<slug:slug>/', views.CompanyList.as_view()),
    path('detail/<slug:slug>/', views.PlaceDetail.as_view()),
]
