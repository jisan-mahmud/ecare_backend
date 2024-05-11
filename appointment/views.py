from rest_framework import viewsets
from .serializers import AppointmentSerializer
from .models import Appointment

class AppointmentViewset(viewsets.ModelViewSet):
    # Specify the queryset and serializer class for the viewset
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        # Get the initial queryset
        queryset = super().get_queryset()

        # Retrieve the 'patient_id' from the query parameters
        patient_id = self.request.query_params.get('patient_id')

        # If 'patient_id' is provided in the query parameters, filter appointments by patient
        if patient_id:
            queryset = queryset.filter(patient__id=patient_id)

        return queryset  # Return the filtered queryset
