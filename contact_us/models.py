from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    
    