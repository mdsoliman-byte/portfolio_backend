from django.db import models

# Create your models here.

# about me 
# name, title , description, image, email, phone, address, website, linkedin, github, twitter, download cv, 
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    website = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    download_cv = models.FileField(upload_to='cv_files/')

# exprience 
# title, company, description, start_date, end_date, 

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
# education
# degree, major, start_date, end_date, university,

class Education(models.Model):
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=100)

# Interests & Specializations
# title , short _description,
class InterestSpecialization(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()


