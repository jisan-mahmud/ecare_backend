from django.db.models.signals import post_save
from .models import Appointment
from django.dispatch import receiver

#Nessasary header file for sent mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender= Appointment)
def save_appointment(sender, instance, **kwargs):
    if instance.appointment_status == 'Running':

        mail_subject = 'Appointment Reminder'
        massage_body = render_to_string('appointment.html', {
            'patient': instance.patient,
            'doctor': instance.doctor,
        })

        to_email = instance.patient.user.email
        email = EmailMessage(
                    subject= mail_subject,
                    body= massage_body,
                    to= [to_email],
                )
        email.content_subtype = 'html'
        email.send()