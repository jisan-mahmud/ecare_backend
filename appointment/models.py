from django.db import models
from doctor.models import Doctor, AvailableTime
from patient.models import Patient

class Appointment(models.Model):
    APPOINTMENT_TYPE = [
        ('Offline', 'Offline'),
        ('Online', 'Online')
    ]
    APPOINTMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Running', 'Running'),
        ('Complete', 'Complete')
    ]
    doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete= models.CASCADE)
    appointment_type = models.CharField(choices= APPOINTMENT_TYPE, max_length= 10)
    appointment_status = models.CharField(choices= APPOINTMENT_STATUS, max_length= 10)
    symtom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete= models.CASCADE)

    class Meta:
        unique_together = ['doctor', 'time', 'patient']

    def __str__(self):
        return f'Patient Name: {self.patient.user.first_name}, Doctor Name: {self.doctor.user.first_name}'
