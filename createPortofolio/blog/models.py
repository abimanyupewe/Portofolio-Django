from django.db import models

class Category(models.Model):
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