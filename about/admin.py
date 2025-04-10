from django.contrib import admin
from .models import Experience, Education, About, Skill # Import the AboutMe model

# Register your models here.

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(About)  # Register the AboutMe model
admin.site.register(Skill)  # Register the Skill model if it exists