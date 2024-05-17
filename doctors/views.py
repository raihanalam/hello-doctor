from django.shortcuts import get_object_or_404, render
from .models import Doctor

# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    print(doctors, '<<<<<<<<<<<<<<<<<<<<<<<,')
    
    context = {
        'doctors': doctors
    }
    
    return render(request, 'doctors/doctor__lisiting.html', context)

def doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
     
    context = {
        'doctor': doctor
    }
    return render(request, 'doctors/doctor.html', context)