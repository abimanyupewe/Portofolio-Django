from django.contrib import admin
from .models import HeroSection, ProjectSection, BlogSection, SkillSection

# Register your models here.

admin.site.register(HeroSection)
admin.site.register(ProjectSection)
admin.site.register(BlogSection)
admin.site.register(SkillSection)