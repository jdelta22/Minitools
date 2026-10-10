"""
URL configuration for setup project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("calculator.urls")),
    path("", include("documents_validator.urls")),
]
