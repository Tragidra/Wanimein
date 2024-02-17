from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('wanimein.api.urls')),
    path('', include('video.urls')),
]
