from django.urls import path
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView)

from .views import RegistrationView


urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('password-change/', PasswordChangeView.as_view(), name='pass_change'),
    
]
