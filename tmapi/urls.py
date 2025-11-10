"""
URL configuration for tmapi project.

"""
from django.urls import path, include

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('logistics.urls')), 
]
