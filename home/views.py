from django.shortcuts import render
from django.views.generic import ListView
from .models import News

# Create your views here.

class HomePage(ListView):
    template_name = 'index.html'
    model = News
