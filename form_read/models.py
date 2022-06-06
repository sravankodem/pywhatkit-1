from django.db import models

# Create your models here.

class ContactForm(models.Model):
    #fullname= models.CharField(max_length=100)
    #email= models.EmailField()
    phone= models.CharField(max_length=50)
    msg = models.CharField(max_length=200)
    