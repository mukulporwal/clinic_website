from django.db import models

# Create your models here.

class fertiService(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    btnname = models.CharField(max_length=100 ,null=True, blank=True)
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class endometriosis(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    btnname = models.CharField(max_length=100 ,null=True, blank=True)
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class laparoscopy(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    btnname = models.CharField(max_length=100 ,null=True, blank=True)
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class riskdelivery(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    btnname = models.CharField(max_length=100 ,null=True, blank=True)
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
