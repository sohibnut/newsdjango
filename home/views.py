from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from .models import News
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import AddNewsForm

# Create your views here.

class HomePage(ListView):
    template_name = 'index.html'
    model = News


class Contact():
    pass

@login_required
def addnewsview(request):
    if request.POST:
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            
    context = {}
    context['form'] = AddNewsForm()
    return render(request, 'add_new.html', context)


