from django.shortcuts import render
from doctors.models import Doctor, FAQ


def index(request):
    doctors = Doctor.objects.all()
    faqs = FAQ.objects.all()
    
    context = {
        'doctors': doctors,
        'faqs': faqs
    }
    return render(request, 'pages/index.html', context)