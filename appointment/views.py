from urllib import response
from rest_framework.views import APIView
from .serializers import AppointmentSerializer, TakeAppointmentSerializer
from .models import Appointment
from patient.models import Patient
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status

class AppointmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk= None, formate= None):
        if pk:
            appointments = Appointment.objects.get(pk= pk)
            serialize_data = AppointmentSerializer(appointments)
        else:
            patient = Patient.objects.get(user= request.user)
            appointments = Appointment.objects.filter(patient= patient)
            serialize_data = AppointmentSerializer(appointments, many= True)
        return Response(serialize_data.data, status= status.HTTP_200_OK)

    def post(self, request):
        patient = Patient.objects.get(user= request.user)
        serializer = TakeAppointmentSerializer(data= request.data, context= {'patient': patient})

        if serializer.is_valid():
            instance = serializer.save(patient= patient)
            instance.save()
            response = {
                'success': True,
                'massage': 'Successfully taken a appointment!'
            }
            return Response(response, status= status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status= status.HTTP_406_NOT_ACCEPTABLE)
    
    def delete(self, request, pk, format= None):
        appointment = Appointment.objects.get(pk= pk)
        print(appointment)
        appointment.delete()
        response = {
            'success': True,
            'massage': 'Cancel appointment successfully'
        }
        return Response(response, status= status.HTTP_204_NO_CONTENT)
