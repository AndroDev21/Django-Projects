from typing_extensions import Self
from django.db import models
# from Emp1.models import self
# Create your models here.
class Emp1(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    middlename= models.CharField(max_length=10)
    emp_id=models.IntegerField()
    def __str__(self):
        return self.firstname 