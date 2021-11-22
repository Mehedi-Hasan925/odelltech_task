from django.db import models
from django.db.models.base import Model

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Divisions(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='divisions')

    def __str__(self):
        return self.name

class Districts(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey(Divisions,on_delete=models.CASCADE,related_name='zila')

    def __str__(self):
        return self.name


class Upazilla(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(Districts,on_delete=models.CASCADE,related_name='thana')
    
    def __str__(self):
        return self.name


class User_info(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True,null=True,related_name='cntry')
    Division = models.ForeignKey(Divisions,on_delete=models.SET_NULL,blank=True,null=True,related_name='dvsn')
    District = models.ForeignKey(Districts,on_delete=models.SET_NULL,blank=True,null=True,related_name='dstrct')
    upazilla = models.ForeignKey(Upazilla,on_delete=models.SET_NULL,blank=True,null=True,related_name='upzla')

    def __str__(self):
        return self.name
