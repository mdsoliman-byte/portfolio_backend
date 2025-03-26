from django.shortcuts import render
from rest_framework import generics
from .models import Project, ProjectCategory
from .serializers import ProjectSerializer, ProjectCategorySerializer

# Create your views here.

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer

class ProjectCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
