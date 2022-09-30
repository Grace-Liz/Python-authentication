from django.db import models

# Create your models here.

class Pythonista(models.Model):
    userName=models.CharField(max_length=50)
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    lastLogin=models.DateTimeField(blank=True, null=True)
