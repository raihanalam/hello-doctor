from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('<int:doctor_id>', views.doctor_profile, name='doctor_profile'),
    path('online-consultancy/<int:doctor_id>/', views.online_consultancy_request, name='online_consultancy_request'),
    # path('search', views.seacrh, name='search'),
    # path('search', views.search, name='search'),
]