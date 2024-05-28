from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

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
    designation = models.ForeignKey(Designation, on_delete= models.CASCADE)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length= 100)


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Review(models.Model):
    STAR_RATING = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    )
    reviewer = models.ForeignKey(Patient, on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    body = models.TextField()
    rating = models.CharField(choices= STAR_RATING, max_length= 7)
    create_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        unique_together = ('reviewer', 'doctor')

    def __str__(self):
        return f'Doctor: {self.doctor.user.first_name} review by {self.reviewer.user.first_name}'
