from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, ProjectCategoryListView

urlpatterns = [
    path('project/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('categories/', ProjectCategoryListView.as_view(), name='project-categories'),
]
