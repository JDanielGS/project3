from django.shortcuts import render
from django.contrib import messages
from .models import NewsLettersUser
from .forms import NewsLetterUserSingUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def NewsLetter_SingUp(request):
    form=NewsLetterUserSingUpForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        if NewsLettersUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'email already exists')
        else:
            instance.save()
            messages.success(request, 'We have sent a email to your emailbox, open to continue your training')
            #Email Message

            subject="Cooking Books"

            from_email=settings.EMAIL_HOST_USER
            to_email=[instance.email]


            html_template=r'C:\Users\usuario\project3\templates\newsletters\email_templates\welcome.html'
            html_message=render_to_string(html_template)

            message=EmailMessage(subject, html_message, from_email, to_email)

            message.content_subtype='html'

            message.send()
    
    context={
        'form':form,
    }

    return render(request, 'start-here.html', context)

def NewslettersUnsuscribe(request):
    form=NewsLetterUserSingUpForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        if NewsLettersUser.objects.filter(email=instance.email).exists():
            NewsLettersUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Your email has been deleted')
        else:
            print('Email Not Found.')
            messages.warning(request, 'Email Not Found.')
    
    context={
        'form':form
    }

    return render(request, 'unsuscribe.html' ,context)

