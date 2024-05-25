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
        fields = [
            'monday', 'monday_start_time', 'monday_end_time',
            'tuesday', 'tuesday_start_time', 'tuesday_end_time',
            'wednesday', 'wednesday_start_time', 'wednesday_end_time',
            'thursday', 'thursday_start_time', 'thursday_end_time',
            'friday', 'friday_start_time', 'friday_end_time',
            'saturday', 'saturday_start_time', 'saturday_end_time',
            'sunday', 'sunday_start_time', 'sunday_end_time'
        ]
        labels = {
            'monday': 'Monday',
            'monday_start_time': 'Monday Start Time',
            'monday_end_time': 'Monday End Time',
            'tuesday': 'Tuesday',
            'tuesday_start_time': 'Tuesday Start Time',
            'tuesday_end_time': 'Tuesday End Time',
            'wednesday': 'Wednesday',
            'wednesday_start_time': 'Wednesday Start Time',
            'wednesday_end_time': 'Wednesday End Time',
            'thursday': 'Thursday',
            'thursday_start_time': 'Thursday Start Time',
            'thursday_end_time': 'Thursday End Time',
            'friday': 'Friday',
            'friday_start_time': 'Friday Start Time',
            'friday_end_time': 'Friday End Time',
            'saturday': 'Saturday',
            'saturday_start_time': 'Saturday Start Time',
            'saturday_end_time': 'Saturday End Time',
            'sunday': 'Sunday',
            'sunday_start_time': 'Sunday Start Time',
            'sunday_end_time': 'Sunday End Time',
        }
