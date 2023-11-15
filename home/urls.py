from django.urls import path
from django.shortcuts import redirect
from .views import HomePage, Contact, addnewsview

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    #path('contactus/', Contact.as_view() , name='contact')
    path('add-new/', addnewsview, name='add_new'),
]
