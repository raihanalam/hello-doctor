from django.contrib import admin
from .models import Speciality, Doctor, Appointment, DoctorAvailability, OnlineConsultancyRequest

admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(DoctorAvailability)
admin.site.register(OnlineConsultancyRequest)



