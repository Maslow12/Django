from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='Login'),
    #path('registro/', register_view.as_view(), name='Registro'),
    path('logout/', login_required(redirect_field_name='login/')(logout_user), name='Logout'),
    path('recover_password/', MissingPassword.as_view(), name='RecoverPassword'),
    path('recover_username/', MissingUsername.as_view(), name='RecoverUsername')
]