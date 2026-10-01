from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Calculator(TemplateView):
    template_name = 'calculator/pages/calculator.html'