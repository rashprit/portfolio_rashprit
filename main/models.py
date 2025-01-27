from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField()
    demo_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=100, blank=True)  # For Bootstrap icons

class Certification(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    date_earned = models.DateField()

