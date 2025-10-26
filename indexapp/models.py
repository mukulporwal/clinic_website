from django.db import models

# Create your models here.

class maincarousel(models.Model):
    image = models.ImageField(upload_to='static/img')


class mainbox(models.Model):
    image_box = models.ImageField(upload_to='static/img', null=True, blank=True)
    title = models.CharField(max_length=200)    
    one_description = models.TextField(max_length=300 , null=True, blank=True)
    two_description = models.TextField(max_length=300 , null=True, blank=True)
    btnname = models.CharField(max_length=100 ,null=True, blank=True)


class difcontent(models.Model):
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300 , null=True, blank=True)