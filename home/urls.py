from django.urls import path
from django.shortcuts import redirect
from .views import HomePage, Contact, addnewsview, CategoryView, DetailView, SearchView


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    #path('contactus/', Contact.as_view() , name='contact')
    path('add-new/', addnewsview, name='add_new'),
    path('news/category/<int:pk>', CategoryView.as_view(), name='category'),
    path('news/detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('search/', SearchView.as_view(), name='search'),
]
