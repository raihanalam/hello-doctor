from django.shortcuts import render
from doctors.models import Doctor, FAQ, Speciality


def index(request):
    doctors = Doctor.objects.all()
    faqs = FAQ.objects.all()
    specialities = Speciality.objects.all()

    
    context = {
        'specialities':specialities,
        'doctors': doctors,
        'faqs': faqs
    }
    return render(request, 'index.html', context)