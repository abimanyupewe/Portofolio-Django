from django.shortcuts import render
from .models import ExperienceSection, HeroSection, SkillSection, ProjectSection, BlogSection

# Create your views here.

def home(request):
    context = {
        'navbar': [
            {'name': 'Home', 'url': '/'},
            {'name': 'Blog', 'url': '/blog/'},
            {'name': 'About', 'url': '/about/'},
            {'name': 'Contact', 'url': '/contact/'},
        ],
        'hero_section': HeroSection.objects.first(),
        'skill_section': SkillSection.objects.all(),
        'project_section': ProjectSection.objects.all(),
        'experience_section': ExperienceSection.objects.all(),
        'blog_section': BlogSection.objects.all(),
    }
    return render(request, 'index.html', context)
