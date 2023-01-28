from django.shortcuts import render
from .forms import NewsLetterUserSingUpForm

def NewsLetter_SingUp(request):
    form=NewsLetterUserSingUpForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)