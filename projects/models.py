from django.db import models
from django.utils.text import slugify


class ProjectCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it doesn't exist
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    project_categories = models.ManyToManyField(ProjectCategory, related_name='projects')
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


