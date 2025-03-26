from django.urls import path
from .views import HomeView

urlpatterns = [
    path('data/', HomeView.as_view(), name='home-data'),
]