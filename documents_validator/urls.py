from django.contrib import admin
from django.urls import path
from .views import Cpf

app_name = 'documentsvalidator'
urlpatterns = [
    path('docvalidator/cpf', Cpf, name="Cpf_validator" ),
]