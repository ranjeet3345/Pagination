from django.db import models

class Customer(models.Model):
    cname=models.CharField(max_length=70)
    cid=models.IntegerField(unique=True)
    cemail=models.EmailField(default="default@gmail.com")
    
