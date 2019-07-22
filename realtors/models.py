from django.db import models

# Create your models here.
class Realtor(models.Model):
    name         = models.CharField(max_length=200)
    email        = models.EmailField(max_length=254)
    description  = models.TextField(blank=True)
    phone        = models.CharField(max_length=20)  
    photo        = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_mvp       = models.BooleanField(default=False)
    hire_date    = models.DateField(auto_now=True, blank=True)  
    def __str__(self):
        return self.name