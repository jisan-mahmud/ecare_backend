from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile_no']

    def name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


admin.site.register(Patient, PatientAdmin)
