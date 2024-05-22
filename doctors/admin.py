from django.contrib import admin
from .models import Speciality, Doctor, Appointment, DoctorAvailability, OnlineConsultancyRequest, Qualification, Expertise, Language, Publication, FAQ

admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(DoctorAvailability)
admin.site.register(OnlineConsultancyRequest)
admin.site.register(Qualification)
admin.site.register(Expertise)
admin.site.register(Language)
admin.site.register(Publication)
admin.site.register(FAQ)



