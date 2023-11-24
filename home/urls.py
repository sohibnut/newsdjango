from django.urls import path
from django.shortcuts import redirect
from .views import (HomePage, CategoryView, DetailView, 
                    SearchView, TagsView, AddNewsView,
                    MyNewsView, UpdateNewsView, DeleteNewsView,
                    AuthorView)


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    #path('contactus/', Contact.as_view() , name='contact')
    path('add-news/', AddNewsView.as_view(), name='add_news'),
    path('my-news/', MyNewsView.as_view(), name='my_news'),
    path('news/category/<int:pk>', CategoryView.as_view(), name='category'),
    path('news/tags/<int:pk>', TagsView.as_view(), name='tag'),
    path('news/detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('news/update/<int:pk>', UpdateNewsView.as_view(), name='update'),
    path('news/delete/<int:pk>', DeleteNewsView.as_view(), name='delete'),
    path('search/', SearchView.as_view(), name='search'),
    path("news/author/<str:slug>", AuthorView.as_view(), name="author"),
]
