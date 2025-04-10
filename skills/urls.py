from django.urls import path
from .views import SkillListCreateView, SkillDetailView, SkillCategoryListView

urlpatterns = [
    path('data/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('<int:id>/', SkillDetailView.as_view(), name='skill-detail'),
    path('categories/', SkillCategoryListView.as_view(), name='skill-categories'),
]
