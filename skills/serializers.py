# # serializers.py
# from rest_framework import serializers
# from .models import SkillCategory, Skill

# class SkillCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SkillCategory
#         fields = ['id', 'name', 'slug']
#         read_only_fields = ('slug',)

# class SkillSerializer(serializers.ModelSerializer):
#     category = SkillCategorySerializer(read_only=True)
#     category_id = serializers.PrimaryKeyRelatedField(
#         queryset=SkillCategory.objects.all(),
#         source='category',
#         write_only=True
#     )

#     class Meta:
#         model = Skill
#         fields = ['id', 'name', 'slug', 'category', 'category_id']
#         read_only_fields = ('slug',)