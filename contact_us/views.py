from rest_framework import serializers
from rest_framework import viewsets
from .serializers import ContactUsSerializer
from .models import ContactUs

class ContactUsViewset(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer