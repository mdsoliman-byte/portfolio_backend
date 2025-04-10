from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Skill, SkillCategory
from .serializers import SkillSerializer, SkillCategorySerializer

class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]

class SkillCategoryListView(generics.ListAPIView):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
