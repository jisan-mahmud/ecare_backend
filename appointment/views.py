from rest_framework import viewsets
from .serializers import AppointmentSerializer
from .models import Appointment

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id', None)
        if patient_id != None:
            queryset = queryset.filter(patient__id = patient_id)
        return queryset
