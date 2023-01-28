from django.urls import path
from .views import NewsLetter_SingUp, NewslettersUnsuscribe


app_name="newsletters"

urlpatterns=[
    path('singup/', NewsLetter_SingUp, name="optin"),
    path('unsuscribe/', NewslettersUnsuscribe, name="unsuscribe"),
    
]