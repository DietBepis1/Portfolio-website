from django.shortcuts import render
from .models import ShowcaseItem, AboutMe

# Create your views here.
def index(request):
    """The homepage for this website"""

    showcase = ShowcaseItem.objects.order_by('-date')
    aboutme = AboutMe.objects.get()
    context = {'showcase': showcase,
                'aboutme': aboutme,
              }
    return render(request, 'software_showcase/index.html', context)

def contact(request):
    """The AboutMe and contact page for the site"""

    aboutme = AboutMe.objects.get()
    context = {'aboutme': aboutme}
    return render(request, 'software_showcase/contact.html', context)