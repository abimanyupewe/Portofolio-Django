from django.shortcuts import render

# Create your views here.

def blog(request):
    context = {
        'title': 'Blog',
        # 'navbar': [
        #     {'name': 'Home', 'url': '/'},
        #     {'name': 'Blog', 'url': '/blog'},
        #     {'name': 'About', 'url': '/about'},
        #     {'name': 'Contact', 'url': '/contact'},
        # ],
    }
    return render(request, 'blog.html', context)