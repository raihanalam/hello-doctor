from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', include('doctors.urls')), 
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]