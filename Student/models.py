from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length= 100)
    gender = models.CharField(max_length=10)
    bio = models.TextField()
    country = models.CharField(max_length=32)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




