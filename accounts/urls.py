"""Defines URL patterns for accounts."""

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [

    # login & logout provided by Django
    path('', include('django.contrib.auth.urls')),

    # registration page
    path('register/', views.register, name='register'),
]
