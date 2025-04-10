from rest_framework import serializers
from .models import Project, ProjectCategory

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    project_categories = ProjectCategorySerializer(many=True, read_only=True)
    project_categories_ids = serializers.PrimaryKeyRelatedField(
        queryset=ProjectCategory.objects.all(),
        source='project_categories',
        many=True,
        write_only=True
    )

    class Meta:
        model = Project
        fields = [
            'id', 'slug', 'title', 'short_description', 'long_description', 'image',
            'project_categories', 'project_categories_ids', 'start_date', 'end_date',
            'url', 'github_url', 'tags'
        ]
