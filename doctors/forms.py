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
        fields = ['patient_name', 'patient_phone_number', 'patient_email', 'doctor', 'appointment_date', 'appointment_time']



# class OnlineConsultancyRequestForm(forms.ModelForm):

#     class Meta:
#         model = OnlineConsultancyRequest
#         fields = ['requested_datetime', 'symptoms']
#         widgets = {
#             'requested_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(OnlineConsultancyRequestForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Request Consultancy'))

class OnlineConsultancyRequestForm(forms.ModelForm):

    
    class Meta:
        model = OnlineConsultancyRequest
        fields = ('patient_name', 'mobile_number', 'email', 'requested_datetime', 'gender', 'symptoms')
        widgets = {
            'requested_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



