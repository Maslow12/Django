from django.contrib import admin
from django.urls import path, include
from Profile.views import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='Profile')
]