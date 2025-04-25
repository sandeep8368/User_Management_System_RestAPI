from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    
    
class ItemModel(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()