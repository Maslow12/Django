from django.shortcuts import  render, redirect
from .forms import UserForm
from .models import User
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt


class RegisterView(TemplateView):
    template_name = 'Register/register.html'
    form_class = UserForm()
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        context= {'form': UserForm}
        form_class = UserForm
        return render(request, 'Register/register.html',context=context)
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST); 
        print(form.errors.as_data())
        if form.cleaned_data['username'] not in list(User.objects.all().values_list('username',flat=True)):
            print(1)
            if form.data['password1'] == form.data['password2']:
                if form.data['email'] not in list(User.objects.all().values_list('email',flat=True)):
                    if form.is_valid():
                        user = form.save()
                        send_mail(
                        'Registro Exitoso',
                        'Se registro satisfactoriamente','gestionbackemail@gmail.com',['yustisebas524@gmail.com'])
                        messages.success(request, 'Registrado correctamente')
                        return redirect(reverse_lazy('Login'))
                    else:
                        messages.error(request, 'Lastimosamente algo salio mal.') 
                        return redirect(reverse_lazy('Register'))
                else:
                    messages.error(request, 'Este correo ya existe')
                    return redirect('Register')
            else:
                messages.error(request, 'Las contrasenas no coincidens')
                return redirect('Register')
        else:
            messages.error(request, 'Este username ya existe')
            return redirect('Register')
        form = UserForm()
        return redirect('Register')