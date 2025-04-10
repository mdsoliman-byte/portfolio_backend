from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

    def validate_skills(self, value):
        # If it's a string inside a list, split it
        if isinstance(value, list) and len(value) == 1 and isinstance(value[0], str):
            return [skill.strip() for skill in value[0].split(',')]
        return value
