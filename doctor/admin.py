from django.contrib import admin
from .models import (
    AvailableTime,
    Designation,
    Specialization,
    Doctor
)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Designation, DesignationAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Doctor)
admin.site.register(AvailableTime)