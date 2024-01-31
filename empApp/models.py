from django.db import models

# Create your models here.
class Employee(models.Model):
    # EmpID = models.CharField(primary_key=True)
    Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Employee_Mo = models.IntegerField()
    Department = models.CharField(max_length=50)

class SampleModel(models.Model):
    SampID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length = 50)
    Age = models.IntegerField()
