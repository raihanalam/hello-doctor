from django.shortcuts import render
from doctors.models import Doctor


def index(request):
    doctors = Doctor.objects.all()
    
    context = {
        'doctors': doctors
    }
    return render(request, 'pages/index.html', context)