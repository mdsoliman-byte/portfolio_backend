from django.contrib import admin
from .models import AboutMe ,Experience, Education # Import the AboutMe model

# Register your models here.

admin.site.register(AboutMe)
admin.site.register(Experience)
admin.site.register(Education)