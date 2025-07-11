from django.shortcuts import render

from .models import ProjectSection

# Create your views here.
def project(request):
    context = {
        'project_section': ProjectSection.objects.all(),
    }
    return render(request, 'project.html', context)