from django.urls import path
from . import views
from .views import doctor_dashboard_view, schedule_meeting_view
from .views import register_doctor, add_doctor_qualifications, add_doctor_expertise,\
      add_doctor_publications, add_doctor_availability, doctor_own_profile,\
      confirm_appointment, consult_appointment, cancel_appointment, confirm_online_consultancy, cancel_online_consultancy



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


    path('appointment/confirm/<int:appointment_id>/', confirm_appointment, name='confirm_appointment'),
    path('appointment/consult/<int:appointment_id>/', consult_appointment, name='consult_appointment'),
    path('appointment/cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),


    path('online-consultancy/confirm/<int:cons_id>/', confirm_online_consultancy, name='confirm_online_consultancy'),
    path('online-consultancy/cancel/<int:cons_id>/', cancel_online_consultancy, name='cancel_online_consultancy'),
]

