from django.db import models

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
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
