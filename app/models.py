from django.db import models

# Create your models here.

class College(models.Model):
    CName=models.CharField(max_length=100,primary_key=True)
    Principal=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    def __str__(self):
        return self.CName

class Student(models.Model):
    CName=models.ForeignKey(College,on_delete=models.CASCADE)
    Sname=models.CharField(max_length=100)
    Sid=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.Sname
    