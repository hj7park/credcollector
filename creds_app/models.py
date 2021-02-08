from django.db import models
from django.urls import reverse
# Create your models here.


class URL(models.Model):
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('urls_detail', kwargs={'pk': self.id})
    

class Cred(models.Model):
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    url = models.ManyToManyField(URL)
    def __str__(self):
        return self.account
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cred_id': self.id})
