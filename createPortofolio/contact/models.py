from django.db import models

class ContactSection(models.Model):
    image = models.ImageField(upload_to='contact_images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Sosmed(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='sosmed_icons/', null=True, blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name