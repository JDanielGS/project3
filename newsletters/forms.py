from django import forms
from .models import NewsLettersUser, NewsLetter

class NewsLetterUserSingUpForm(forms.ModelForm):
    class Meta:
        model=NewsLettersUser
        fields=['email']

class NewsLetterCreationForm(forms.ModelForm):
    class Meta:
        model=NewsLetter
        fields=['name','subject','body','email']