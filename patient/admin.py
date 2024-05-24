from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'gender', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    list_filter = ('gender', 'date_of_birth')

admin.site.register(Patient, PatientAdmin)
