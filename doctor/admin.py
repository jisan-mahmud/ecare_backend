from django.contrib import admin
from .models import (
    AvailableTime,
    Designation,
    Specialization,
    Doctor,
    Review
)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation']
    list_filter = ('designation', 'specialization')
    search_fields = ('user__first_name', 'user__last_name')

    def name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

admin.site.register(Designation, DesignationAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(AvailableTime)
admin.site.register(Review)