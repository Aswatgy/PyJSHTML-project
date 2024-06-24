from django.db import models
from django.db import models

class regtb_user(models.Model):
    username=models.CharField(max_length=50)
    mobilenumber=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)

# Create your models here.
