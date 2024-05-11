from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from patient.models import Patient

@receiver(post_save, sender= User)
def add_patient(sender, instance, **kwargs):
    if instance.is_active == True:
        if Patient.objects.filter(user= instance).exists() == False:
            Patient.objects.create(user= instance)