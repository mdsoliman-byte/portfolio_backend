from django.urls import path
from .views import AboutMeView, AboutDataView, AboutUpdateView
from . import views

urlpatterns = [
    path('data/', AboutDataView.as_view(), name='about-data'),
    path('update/', AboutUpdateView.as_view(), name='about-update'),
]
