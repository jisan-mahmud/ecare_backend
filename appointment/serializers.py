from rest_framework import serializers
from .models import Appointment
from django.db.models import Q

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField(many= False)
    patient = serializers.StringRelatedField(many= False)
    time = serializers.StringRelatedField(many= False)
    class Meta:
        model = Appointment
        fields = '__all__'


class TakeAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_type', 'symtom', 'time']

    def validate(self, attrs):
        time = attrs['time']
        doctor = attrs['doctor']
        patient = self.context.get('patient')
        appointment = Appointment.objects.filter(Q(time= time) & Q(patient= patient) & Q(doctor= doctor)).order_by('-date')
        if appointment.exists() and appointment[0].appointment_status != 'Complete':
            raise serializers.ValidationError({'Un_field': 'You have already take a appointment!'})
        return attrs

    def create(self, validated_data):
        instance = Appointment(**validated_data)

        return instance