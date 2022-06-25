from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'Recover'

urlpatterns = [
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Recover/password_reset_success.html'), name='password_reset_success'),
    path('accounts/recover/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Recover/password_reset_confirm.html"), name='password_reset_confirm'),
    path('accounts/recover/', auth_views.PasswordResetView.as_view(template_name="Recover/password_reset.html"), name='account_reset_password'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Recover/password_reset_complete.html'), name='password_reset_complete'),      
]