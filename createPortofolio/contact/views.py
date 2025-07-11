from django.shortcuts import render
from .models import ContactSection, Sosmed

# Create your views here.
def contact(request):
    context = {
        'title': 'Contact',
        'contact_section': ContactSection.objects.all(),
        'sosmed_section': Sosmed.objects.all()
    }
    return render(request, 'contact.html', context)