from django.db import models

# Create your models here.

class add_cam(models.Model):
    id=models.AutoField(primary_key=True)
    brand=models.CharField(max_length=20)
    cam_models=models.CharField(max_length=30)
    formfactor=models.CharField(max_length=20)
    resolution=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    opticalzoom=models.CharField(max_length=10)

class add_lens(models.Model):
    id=models.AutoField(primary_key=True)
    brand=models.CharField(max_length=20)
    lenstype=models.CharField(max_length=30)
    mount=models.CharField(max_length=20)
    maxflength=models.CharField(max_length=20)
    minflength=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    
class user_login(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    
class admin_login(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class admn_lgin(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)