from django.urls import path

from .views import cpf_validator, cnpj_validator

app_name = "documents_validator"

urlpatterns = [
    path("documents/cpf/", cpf_validator, name="cpf_validator"),
    path("documents/cnpj/", cnpj_validator, name="cnpj_validator"),

]
