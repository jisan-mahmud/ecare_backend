from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'Patient')
    image = models.ImageField(upload_to= 'patient/image', blank= True)
    mobile_no = models.CharField(max_length= 12, blank= True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
