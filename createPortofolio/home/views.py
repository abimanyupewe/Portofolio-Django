from django.shortcuts import render
from .models import HeroSection, ProjectSection, BlogSection, SkillSection

# Create your views here.

def home(request):
    hero_section = HeroSection.objects.first()
    project_section = ProjectSection.objects.all()
    blog_section = BlogSection.objects.all()
    skill_section = SkillSection.objects.all()
    context = {
        'hero_section': hero_section,
        'project_section': project_section,
        'blog_section': blog_section,
        'skill_section': skill_section,
    }
    return render(request, 'index.html', context)