from django.db import models

class About(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.JSONField(default=list, help_text="List of bio sentences")
    profile_image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    contact_location = models.CharField(max_length=255)
    contact_email = models.EmailField()
    available_for_freelance = models.BooleanField(default=True)
    social_github = models.URLField(blank=True, null=True)
    social_twitter = models.URLField(blank=True, null=True)
    social_linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class Experience(models.Model):
    about = models.ForeignKey(About, related_name="experience", on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    description = models.JSONField(default=list, help_text="List of details")

    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    about = models.ForeignKey(About, related_name="education", on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Skill(models.Model):
    about = models.ForeignKey(About, related_name="skills", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


