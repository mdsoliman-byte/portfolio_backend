from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, ProjectCategoryListCreateView, ProjectCategoryDetailView

urlpatterns = [
    path('project/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projectCategories/', ProjectCategoryListCreateView.as_view(), name='category-list-create'),
    path('projectCategories/<int:pk>/', ProjectCategoryDetailView.as_view(), name='category-detail'),
]
