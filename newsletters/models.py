from django.db import models

class NewsLettersUser(models.Model):
    email=models.EmailField(null=False, unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class NewsLetter(models.Model):
    name=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    body=models.TextField(blank=True, null=True)
    email=models.ManyToManyField(NewsLettersUser)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name