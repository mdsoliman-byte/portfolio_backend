from django.urls import path
from .views import AboutMeView
from . import views

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('experience/', views.ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('education/', views.EducationListCreateView.as_view(), name='education-list-create'),
]
