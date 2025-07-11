from django.db import models

# Create your models here.

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    span = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    imageProfile = models.ImageField(upload_to='hero_images/')
    available_for_work = models.BooleanField(default=False)
    custom_text = models.CharField(max_length=50, default="Available for Work")
    working_on = models.CharField(max_length=200, null=True, blank=True)
    experience = models.PositiveIntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='hero_sections', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class SkillSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='skill_images/')

    def __str__(self):
        return self.title

class ExperienceSection(models.Model):
    image = models.ImageField(upload_to='experience_images/', blank=True, null=True)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='experience_sections', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False, verbose_name="Currently Working")

    def __str__(self):
        return f"{self.company} - {self.position}"
    
class ProjectSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    textBtn = models.CharField(max_length=50, default="View Project")
    link = models.URLField(blank=True, null=True)
    stack = models.ForeignKey('Stack', on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    language = models.ForeignKey('LanguageProgramming', on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    framework = models.ForeignKey('Framework', on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name='projects', null=True, blank=True)

    def __str__(self):
        return self.title
    
class LanguageProgramming(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Stack(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class BlogSection(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title