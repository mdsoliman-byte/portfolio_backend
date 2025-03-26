# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .models import Skill, SkillCategory
# from .serializers import SkillSerializer, SkillCategorySerializer

# class SkillListCreateView(generics.ListCreateAPIView):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class SkillCategoryListCreateView(generics.ListCreateAPIView):
#     queryset = SkillCategory.objects.all()
#     serializer_class = SkillCategorySerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class SkillCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SkillCategory.objects.all()
#     serializer_class = SkillCategorySerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAuthenticatedOrReadOnly]
