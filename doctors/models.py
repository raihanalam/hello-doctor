from django.db import models
from django.contrib.auth.models import User
from datetime import time
from django.core.files.base import ContentFile

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name
class Language(models.Model):
    # doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.language}"
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    full_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True)
    hospital = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='doctors/')
    languages = models.ManyToManyField(Language)
    bio = models.TextField()
    experience_year = models.IntegerField(default=0)
    availability_start_time = models.TimeField(default=time(9, 0))
    availability_end_time = models.TimeField(default=time(17, 0))
    chamber_address = models.CharField(max_length=464, verbose_name = "Chamber Address")
    is_active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
        
class Qualification(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} from {self.institution} ({self.year})"

class Expertise(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return f"Expertise in {self.speciality.name} - {self.doctor.full_name}"


class Publication(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    journal = models.CharField(max_length=255)
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.journal} ({self.publication_date})"



class DoctorAvailability(models.Model):
    doctor = models.OneToOneField('Doctor', on_delete=models.CASCADE)
    monday = models.BooleanField(default=True)
    monday_start_time = models.TimeField(default=time(9, 0))
    monday_end_time = models.TimeField(default=time(17, 0))
    
    tuesday = models.BooleanField(default=True)
    tuesday_start_time = models.TimeField(default=time(9, 0))
    tuesday_end_time = models.TimeField(default=time(17, 0))
    
    wednesday = models.BooleanField(default=True)
    wednesday_start_time = models.TimeField(default=time(9, 0))
    wednesday_end_time = models.TimeField(default=time(17, 0))
    
    thursday = models.BooleanField(default=True)
    thursday_start_time = models.TimeField(default=time(9, 0))
    thursday_end_time = models.TimeField(default=time(17, 0))
    
    friday = models.BooleanField(default=True)
    friday_start_time = models.TimeField(default=time(9, 0))
    friday_end_time = models.TimeField(default=time(17, 0))
    
    saturday = models.BooleanField(default=False)
    saturday_start_time = models.TimeField(default=time(9, 0))
    saturday_end_time = models.TimeField(default=time(17, 0))
    
    sunday = models.BooleanField(default=False)
    sunday_start_time = models.TimeField(default=time(9, 0))
    sunday_end_time = models.TimeField(default=time(17, 0))

    def __str__(self):
        return f"Availability for {self.doctor.full_name}"

    

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name='patient_appointments', blank=True, null=True)
    patient_name = models.CharField(max_length=255)
    patient_phone_number = models.CharField(max_length=15)
    patient_email = models.EmailField(blank=True,)
    patient_image = models.ImageField(upload_to='patient_image', blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_status = (
        ('booked', 'Booked'),
        ('confirmed', 'Confirmed'),
        ('consulted', 'Consulted'),
        ('canceled', 'Canceled')
    )
    status = models.CharField(choices = appointment_status, default='booked', max_length=10)

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=gender_choices)
    symptoms = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('doctor', 'appointment_date', 'appointment_time')

    def __str__(self):
        return f"Appointment with {self.doctor.full_name} on {self.appointment_date} at {self.appointment_time}"    
    
    def save(self, *args, **kwargs):
        if isinstance(self.patient_image, bytes):
            self.patient_image = ContentFile(self.patient_image)
        super().save(*args, **kwargs)


class OnlineConsultancyRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    requested_datetime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # patient = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255, verbose_name = 'Patient Name')
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=gender_choices)
    symptoms = models.TextField()

    def __str__(self):
        return f'{self.patient_name} - {self.doctor.full_name} - {self.status}'
    
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question