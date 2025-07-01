from django.shortcuts import render

# Create your views here.
def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', context)