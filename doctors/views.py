from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Doctor, OnlineConsultancyRequest
from .forms import OnlineConsultancyRequestForm, AppointmentForm


from django.contrib import messages

# Create your views here.
def doctor_list(request):
    doctors = Doctor.objects.all()
    
    context = {
        'doctors': doctors
    }
    
    return render(request, 'doctors/doctor_lisit.html', context)

def doctor_profile(request, doctor_id):
    form = OnlineConsultancyRequestForm()

    doctor = get_object_or_404(Doctor, pk=doctor_id)


     
    context = {
        'form': form, 
        'doctor': doctor
    }
    return render(request, 'doctors/doctor_profile.html', context)


def online_consultancy_request(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = OnlineConsultancyRequestForm(request.POST)
        if form.is_valid():
            consultancy_request = form.save(commit=False)
            consultancy_request.doctor = doctor  # Assign the doctor object
            consultancy_request.save()
            messages.success(request, 'Your request is successfully submitted. You will get a call for assiatance.')
        else:
            messages.error(request, 'There is a problem to get online consultany. Please try agian later.')
    else:
        form = OnlineConsultancyRequestForm()

    context = {
        'form': form,
        'doctor': doctor
    }
    return render(request, 'doctors/doctor_profile.html', context)


def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.save()
            messages.success(request, 'Appointment Succesfully Booked!')  # Assuming you have a success page
    else:
        form = AppointmentForm()
    
    return render(request, 'doctors/appointment.html', {'form': form})

