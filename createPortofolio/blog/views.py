from django.shortcuts import render
from .models import BlogSection

# Create your views here.

def blog(request):
    context = {
        'title': 'Blog',
        'blog_section': BlogSection.objects.all(),
    }
    return render(request, 'blog.html', context)