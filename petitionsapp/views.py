from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

def PetitionView(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            content=form.cleaned_data
            message = 'Asunto: ' + content['asunto']+ ' ' + ' Enviado por: '+ content['email'] + '\n' + 'Mensaje: ' +content['mensaje']
            send_mail(content['asunto'], message,
            content.get('email','send@gmail.com'),['recive@gmail.com'],)
            messages.success(request, F"El mensaje se envio correctamente.")            
    else:
        form=ContactForm()

    return render(request,"contact.html",{"form":form})
