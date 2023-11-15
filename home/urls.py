from django.urls import path
from django.shortcuts import redirect
from .views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home')
]
