from rest_framework import viewsets
from .serializers import AppointmentSerializer
from .models import Appointment

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer