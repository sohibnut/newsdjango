from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import RegistrationForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View

# Create your views here.
class RegistrationView(CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = RegistrationForm
    
    success_url = reverse_lazy('home')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id = request.user.id)
        context = {
            'user': user,
        }
        return render(request, 'registration/profile.html', context)

class UpdateProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('home')
     
    def test_func(self):
        user = self.get_object()
        if self.request.user == user or self.request.user.is_superuser:
            return True
        return False


