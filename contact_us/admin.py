from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']

admin.site.register(ContactUs, ContactUsAdmin)