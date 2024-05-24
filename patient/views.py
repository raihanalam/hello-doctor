from django.shortcuts import render
from doctors.models import Appointment

# Create your views here.
def appointment_list(request):

     appointment_list = Appointment.objects.filter()

     return render(request, 'appointment_list.html')