from django import forms
from .models import Doctor, Appointment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import OnlineConsultancyRequest
from .models import Doctor, Qualification, Expertise, Publication, DoctorAvailability


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


class DoctorBasicInfoForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'degree', 'speciality', 'hospital', 'phone_number', 'image', 'bio', 'experience_year', 'chamber_address', 'languages']
        labels = {
            'full_name': 'Full Name',
            'degree': 'Degree',
            'speciality': 'Speciality',
            'hospital': 'Hospital',
            'phone_number': 'Phone Number',
            'image': 'Profile Picture',
            'bio': 'Biography',
            'experience_year': 'Years of Experience',
            'chamber_address': 'Chamber Address',
            'languages': 'Languages Spoken',
        }

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['degree', 'institution', 'year']
        labels = {
            'degree': 'Degree',
            'institution': 'Institution',
            'year': 'Year of Graduation',
        }

class ExpertiseForm(forms.ModelForm):
    class Meta:
        model = Expertise
        fields = ['speciality', 'details']
        labels = {
            'speciality': 'Speciality',
            'details': 'Details',
        }

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'journal', 'publication_date']
        labels = {
            'title': 'Title',
            'journal': 'Journal',
            'publication_date': 'Publication Date',
        }

class DoctorAvailabilityForm(forms.ModelForm):
    class Meta:
        model = DoctorAvailability
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        labels = {
            'monday': 'Monday',
            'tuesday': 'Tuesday',
            'wednesday': 'Wednesday',
            'thursday': 'Thursday',
            'friday': 'Friday',
            'saturday': 'Saturday',
            'sunday': 'Sunday',
        }
