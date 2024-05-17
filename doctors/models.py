from django.db import models
from django.contrib.auth.models import User
from datetime import time

class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True)
    hospital = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='doctors/')
    bio = models.TextField()
    availability_start_time = models.TimeField(default=time(9, 0))
    availability_end_time = models.TimeField(default=time(17, 0))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_phone_number = models.CharField(max_length=15)
    patient_email = models.EmailField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('doctor', 'appointment_date', 'appointment_time')

    def __str__(self):
        return f"Appointment with {self.doctor.full_name} on {self.appointment_date} at {self.appointment_time}"

class DoctorAvailability(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    def __str__(self):
        return f"Availability for {self.doctor.full_name}"
