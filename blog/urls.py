from django.urls import path
from .views import (BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('post/new/', BlogCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
]