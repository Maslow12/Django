from django.contrib import admin
from django.urls import path, include
from Register.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='Register')
]