from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductCategoryListView

urlpatterns = [
    path('data/', ProductListCreateView.as_view(), name='product-list-create'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', ProductCategoryListView.as_view(), name='product-categories'),
]
