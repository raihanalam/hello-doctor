from django.urls import path
from . import views
from .views import doctor_dashboard_view, schedule_meeting_view
from .views import register_doctor, add_doctor_qualifications, add_doctor_expertise, add_doctor_publications, add_doctor_availability, doctor_own_profile



app_name = 'doctors'

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('<int:doctor_id>', views.doctor_profile, name='doctor_profile'),
    path('online-consultancy/<int:doctor_id>/', views.online_consultancy_request, name='online_consultancy_request'),
    path('book-appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('doctor-dashboard/', doctor_dashboard_view, name='doctor_dashboard'),
    path('schedule-meeting/', schedule_meeting_view, name='schedule_meeting'),

    path('doctor-profile/',doctor_own_profile, name='own_profile'),

    path('register/basic-info/', register_doctor, name='register_doctor'),
    path('add-qualifications/', add_doctor_qualifications, name='add_doctor_qualifications'),
    path('add-expertise/', add_doctor_expertise, name='add_doctor_expertise'),
    path('add-publications/', add_doctor_publications, name='add_doctor_publications'),
    path('add-availability/', add_doctor_availability, name='add_doctor_availability'),
]

