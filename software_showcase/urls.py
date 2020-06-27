"""Defines url patterns for the main part of the website"""

from django.urls import path
from . import views

app_name = 'software_showcase'

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact')
]
