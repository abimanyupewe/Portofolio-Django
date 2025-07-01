from django.shortcuts import render

# Create your views here.
def project(request):
    context = {
        'title': 'Project',
    }
    return render(request, 'project.html', context)