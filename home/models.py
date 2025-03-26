# Create your models here.
from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100, default="Data Scientist & Programmer")
    shortbio = models.TextField(max_length=153)
    skills = models.JSONField(default=list)
    available_for_freelance = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.title
