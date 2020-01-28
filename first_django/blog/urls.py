from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<post_id>/', views.detail, name='blog_detail'),
]
