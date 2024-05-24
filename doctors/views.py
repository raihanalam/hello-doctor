from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Doctor, OnlineConsultancyRequest
from .forms import OnlineConsultancyRequestForm, AppointmentForm

from django.shortcuts import render, redirect
from .models import Appointment, OnlineConsultancyRequest
from patient.models import Patient
from django.contrib.auth.models import User

from .models import Doctor
from .forms import DoctorBasicInfoForm, QualificationForm, ExpertiseForm, PublicationForm, DoctorAvailabilityForm

from .models import Doctor, Qualification, Expertise, Publication, DoctorAvailability

from django.contrib import messages

# Create your views here.
def doctor_list(request):
    doctors = Doctor.objects.all()
    
    context = {
        'doctors': doctors
    }
    
    return render(request, 'doctor_lisit.html', context)

def doctor_profile(request, doctor_id):
    form = OnlineConsultancyRequestForm()
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    
    try:
        doctoravailability = DoctorAvailability.objects.get(doctor=doctor)
    except:
        doctoravailability=[]

     
    context = {
        'form': form, 
        'doctor': doctor,
        'doctoravailability': doctoravailability,
    }
    return render(request, 'doctor_profile.html', context)


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
    return render(request, 'doctor_profile.html', context)


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
    
    return render(request, 'appointment.html', {'form': form})






def doctor_dashboard_view(request):
    # Fetch data for the dashboard

    doctor = Doctor.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor)
    consultations = OnlineConsultancyRequest.objects.filter(doctor=doctor)
    notifications = []  # Populate this with your logic
    consulted_patients = []  # Populate this with your logic
    patients = Patient.objects.all()  # Assuming you have a Patient model

    context = {
        'doctor':doctor,
        'appointments': appointments,
        'consultations': consultations,
        'notifications': notifications,
        'consulted_patients': consulted_patients,
        'patients': patients,
    }

    return render(request, 'doctor_dashboard.html', context)

def schedule_meeting_view(request):
    if request.method == 'POST':
        patient_id = request.POST['patient']
        meeting_time = request.POST['meeting_time']
        # Add logic to create a Google Meet meeting
        # Redirect to the dashboard after scheduling
        return redirect('doctor_dashboard')
    return redirect('doctor_dashboard')


@login_required
def register_doctor(request):
    if request.method == 'POST':
        form = DoctorBasicInfoForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('doctors:own_profile')
    else:
        form = DoctorBasicInfoForm()
    return render(request, 'register_doctor.html', {'form': form})

@login_required
def doctor_own_profile(request):
    doctor = Doctor.objects.get(user=request.user)
    qualification = Qualification.objects.filter(doctor=doctor)
    expertise = Expertise.objects.filter(doctor=doctor)
    publication = Publication.objects.filter(doctor=doctor)

    context = {

        'doctor':doctor,
        'qualification':qualification,
        'expertise': expertise,
        'publication': publication

    }
    return render(request, 'doctor_own_profile.html', context)

@login_required
def add_doctor_qualifications(request):
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.doctor = request.user.doctor
            qualification.save()
            messages.success(request, 'Your Qulification Successfully Added!')
            return redirect('doctors:own_profile')
    else:
        form = QualificationForm()
    return render(request, 'add_qualifications.html', {'form': form})

@login_required
def add_doctor_expertise(request):
    if request.method == 'POST':
        form = ExpertiseForm(request.POST)
        if form.is_valid():
            expertise = form.save(commit=False)
            expertise.doctor = request.user.doctor
            expertise.save()
            return redirect('doctors:own_profile')
    else:
        form = ExpertiseForm()
    return render(request, 'add_expertise.html', {'form': form})

@login_required
def add_doctor_publications(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.doctor = request.user.doctor
            publication.save()
            return redirect('doctors:own_profile')
    else:
        form = PublicationForm()
    return render(request, 'add_publications.html', {'form': form})

@login_required
def add_doctor_availability(request):
    if request.method == 'POST':
        form = DoctorAvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.doctor = request.user.doctor
            availability.save()
            messages.success(request, 'You have successfully added your avilability!')
            return redirect('doctors:own_profile')
    else:
        form = DoctorAvailabilityForm()
    return render(request, 'add_availability.html', {'form': form})

