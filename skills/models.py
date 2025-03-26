# # models.py
# from django.db import models
# from django.utils.text import slugify

# class SkillCategory(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     slug = models.SlugField(max_length=100, unique=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name

# class Skill(models.Model):  # Changed from Skills to Skill
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
#     slug = models.SlugField(max_length=100, unique=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name