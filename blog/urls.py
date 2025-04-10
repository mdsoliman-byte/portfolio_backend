from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView, BlogCategoryListView

urlpatterns = [
    path('data/', BlogPostListCreateView.as_view(), name='blog-list-create'),
    path('<slug:slug>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('categories/', BlogCategoryListView.as_view(), name='blog-categories'),
]