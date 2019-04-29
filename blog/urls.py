from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('post/<slug:slug>/', views.PostDetail.as_view()),
    path('tag/<slug:slug>/', views.TaggedList.as_view()),
#    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]
