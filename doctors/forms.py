from django import forms
from .models import Doctor, Appointment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import OnlineConsultancyRequest

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['user', 'full_name', 'degree', 'speciality', 'hospital', 'phone_number', 'image', 'bio', 'availability_start_time', 'availability_end_time', 'is_active']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_phone_number', 'patient_email', 'patient_image', 'appointment_date', 'appointment_time', 'gender', 'symptoms']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }



class OnlineConsultancyRequestForm(forms.ModelForm):

    
    class Meta:
        model = OnlineConsultancyRequest
        fields = ('patient_name', 'mobile_number', 'email', 'requested_datetime', 'gender', 'symptoms')
        widgets = {
            'requested_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



