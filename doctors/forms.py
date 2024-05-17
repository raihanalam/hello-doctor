from django import forms
from .models import Doctor, Appointment

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['user', 'full_name', 'degree', 'speciality', 'hospital', 'phone_number', 'image', 'bio', 'availability_start_time', 'availability_end_time', 'is_active']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_phone_number', 'patient_email', 'doctor', 'appointment_date', 'appointment_time']
