from django.contrib import admin
from appointment.models import Appointment
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'time']
    list_filter = ['appointment_status', 'appointment_type']
    search_fields = ['patient__user__first_name', 'doctor__user__first_name', 'appointment_status', 'appointment_type']