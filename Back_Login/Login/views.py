from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView
from Login.forms import *
from django.core.mail import send_mail
from Register.forms import UserForm
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode


class LoginView(FormView):
    template_name = "Login/login.html"
    success_url = reverse_lazy('Index')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form_class = LoginForm()
        return render(request, 'Login/login.html', {'form': form_class})
        
    def post(self, request, *args, **kwargs):  
        form_class = LoginForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, 'Usuario o correo invalido')
            return HttpResponseRedirect(reverse_lazy('Login'))
        
class MissingPassword(TemplateView):
    template_name = 'Login/Reset/reset_password.html'
    def get(self, request):
        form = UserForm()
        return render(request, 'Login/Reset/reset_password.html', {'form': form})

    def post(self,request):
        form = UserForm(request.POST)
        if form.data.get('email') not in list(User.objects.all().values_list('email', flat=True)):
            send_mail('Prueba', 'Este es el mensaje de prueba...', settings.EMAIL_HOST_USER, recipient_list=['yustisebas524@gmail.com'], html_message=render_to_string('Recover/email.html', context={'token':PasswordResetTokenGenerator, 'uid': urlsafe_base64_encode('uidb64'.encode('ascii'))}))
            messages.success(request, 'Las indicaciones fueron enviadas a su correo...')
            return HttpResponseRedirect(reverse_lazy('Login')) #Provicional crear una app que lea el codigo generado
        else:
            messages.error(request, 'El correo no existe...')
            return HttpResponseRedirect(reverse_lazy('RecoverPassword'))
        
class MissingUsername(TemplateView):
    template_name = 'Login/Reset/get_username.html'
    def get(self, request):
        form = UserForm()
        return render(request, 'Login/Reset/get_username.html', {'form': form})

    def post(self,request):
        form = UserForm(request.POST)
        if form.data.get('email') not in list(User.objects.all().values_list('email', flat=True)):
            send_mail('Prueba', 'Este es el mensaje de prueba', settings.EMAIL_HOST_USER, recipient_list=['yustisebas524@gmail.com'])
            messages.success(request, 'Las indicaciones de recuperacion del usuario fueron enviadas a su correo...')
            return HttpResponseRedirect(reverse_lazy('Login')) #Provicional crear una app que lea el codigo generado
        else:
            messages.error(request, 'El correo no existe...')
            return HttpResponseRedirect(reverse_lazy('RecoverPassword'))
        
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('Login'))


    
