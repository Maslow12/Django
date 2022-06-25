from django.shortcuts import render
from django.views.generic.base import TemplateView
from Register.models import User

class ProfileView(TemplateView):
    template_name = 'Profile/profile.html'
    def get(self, request):
        user = User
        return render(request, 'Profile/profile.html', {'user':user})