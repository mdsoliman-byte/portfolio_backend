from django.urls import path
from .views import HomeView, HomeUpdateView

urlpatterns = [
    path('data/', HomeView.as_view(), name='home-data'),
    path('update/', HomeUpdateView.as_view(), name='home-update'),
]