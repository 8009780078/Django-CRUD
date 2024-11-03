from django.db import models

class User(models.Model):
    name= models.CharField(max_length=70, blank = False, null = False)
    email= models.EmailField(max_length=80)
    password= models.CharField(max_length=90, blank = False, null = False)

# Create your models here.
