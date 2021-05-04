
from django.conf import settings
from django.core.mail import  send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado


def inicio(request):
    titulo = "HOLA"
    abc = "123"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)

    context = {
            "titulo": titulo,
            "el_form": form,
        }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "PERSONA"
        instance.save()

        context = {
            "titulo": "Gracias %s!" %(nombre)
        }

        if not nombre:
            context={
                "titulo": "Gracias persona sin nombre"
            }

        print (instance)
        print (instance.timestamp)
   
        obj = Registrado()
        obj.email = abc
    
    return render(request, "base.html" , context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print key
        #     print form.cleaned_data.get(key)
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form de contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "sbenavides543@unab.edu.co"]
        email_mensaje =  "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto, 
            email_mensaje, 
            email_from,
            email_to,
            fail_silently=False
        )
        print (email, mensaje, nombre)
    context = {
        "form": form,
    }

    return render(request, "forms.html", context )