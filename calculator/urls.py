from django.contrib import admin
from django.urls import path
from .views import Calculator

urlpatterns = [
    path('calculator/', Calculator, name="calculator" ),
]
