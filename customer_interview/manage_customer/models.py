from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    def __str__(self):
        return self.first_name
    
    