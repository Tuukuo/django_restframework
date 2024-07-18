from django.db import models

# Create your models here.

class Classroom(models.Model):
  class_name= models.CharField(max_length=20)
  number_of_seats= models.IntegerField()
  number_of_students= models.IntegerField()
  class_teacher= models.CharField(max_length=20)
  course= models.CharField(max_length=25)
  available_equipments= models.TextField()
  description = models.TextField()
  start_time = models.IntegerField()
  end_time = models.IntegerField()
  classroom = models.CharField(max_length= 25)
  day_of_the_week = models.IntegerField()
def __str__(self):
  return f"{self.class_name}"