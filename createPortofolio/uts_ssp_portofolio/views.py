from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'navbar': [
            {'name': 'Home', 'url': '/'},
            {'name': 'Blog', 'url': '/blog'},
            {'name': 'About', 'url': '/about'},
            {'name': 'Contact', 'url': '/contact'},
        ]}
    

    return render(request, 'index.html', context)