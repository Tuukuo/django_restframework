from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length= 100)
    gender = models.CharField(max_length=10)
    bio = models.TextField()
    teacher_id = models.IntegerField()
    country = models.CharField(max_length=32)
    subject_teaching = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"