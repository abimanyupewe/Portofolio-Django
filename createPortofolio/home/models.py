from django.db import models

# Create your models here.

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hero_images/')
    button_text = models.CharField(max_length=100)
    button_link = models.URLField()

    def __str__(self):
        return self.title

class ProjectSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField()

    def __str__(self):
        return self.title

class BlogSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    link = models.URLField()

    def __str__(self):
        return self.title
    
class SkillSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='skill_images/')
    link = models.URLField()

    def __str__(self):
        return self.title