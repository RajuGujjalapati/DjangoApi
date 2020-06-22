from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=23)
    location = models.CharField(max_length=23)

    def __str__(self):
        return self.name +" is loaction in"+self.location

class Employee(models.Model):
    name = models.CharField(max_length=20)
    Age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)