from django.contrib import admin
from django.urls import path
from .views import Calculator

app_name = 'calculator'
urlpatterns = [
    path('calculator/', Calculator, name="calculator" ),
]
