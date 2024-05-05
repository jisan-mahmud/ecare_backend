from django.db import models
from django.contrib.auth.models import User

class Specialization(models.Model):
    name = models.CharField(max_length= 40)
    slug = models.CharField(max_length= 60)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length= 40)
    slug = models.CharField(max_length= 60)

    def __str__(self):
        return self.name


class AvailableTime(models.Model):
    name = models.CharField(max_length= 70)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to= 'doctor/images/')
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ForeignKey(AvailableTime, on_delete= models.CASCADE)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length= 100)

    def __str__(self):
        return f'Dr. {self.user.first_name} {self.user.last_name}'
