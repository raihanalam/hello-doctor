from django.urls import path
from . import views
from .views import choose_role_view

app_name = 'account'

urlpatterns = [
    path('signup', views.sign_up, name='sign_up'),
    path('signin',views.sign_in, name='sign_in'),
    path('signout',views.sign_out,name='sign_out'),

    path('choose-role/', choose_role_view, name='choose_role'),
]

