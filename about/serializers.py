from rest_framework import serializers
from .models import About, Experience, Education, Skill

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'position', 'company', 'period', 'description']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'degree', 'institution', 'period', 'description']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title', 'description']

class AboutSerializer(serializers.ModelSerializer):
    experience = ExperienceSerializer(many=True)
    education = EducationSerializer(many=True)
    skills = SkillSerializer(many=True)

    class Meta:
        model = About
        fields = [
            'id',
            'full_name',
            'title',
            'bio',
            'profile_image',
            'experience',
            'education',
            'skills',
            'contact_location',
            'contact_email',
            'available_for_freelance',
            'social_github',
            'social_twitter',
            'social_linkedin',
        ]

    def update(self, instance, validated_data):
        exp_data = validated_data.pop('experience', [])
        edu_data = validated_data.pop('education', [])
        skill_data = validated_data.pop('skills', [])

        # Update About fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Replace nested Experience list:
        instance.experience.all().delete()
        for exp in exp_data:
            Experience.objects.create(about=instance, **exp)

        # Replace nested Education list:
        instance.education.all().delete()
        for edu in edu_data:
            Education.objects.create(about=instance, **edu)

        # Replace nested Skill list:
        instance.skills.all().delete()
        for skill in skill_data:
            Skill.objects.create(about=instance, **skill)

        return instance
