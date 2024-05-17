from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='doctors'),
    path('<int:doctor_id>', views.doctor, name='doctor'),
    # path('search', views.seacrh, name='search'),
    # path('search', views.search, name='search'),
]