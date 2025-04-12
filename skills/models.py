# models.py
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)  # New field
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    progress = models.PositiveSmallIntegerField(blank=True, null=True, validators=[
        MaxValueValidator(100), MinValueValidator(0)])  # New field


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name