from rest_framework import serializers
from .models import (
    Doctor,
    Designation,
    Specialization,
    AvailableTime,
    Review
)

class DoctorSerializer(serializers.ModelSerializer):
    specialization = serializers.StringRelatedField(many= True)
    designation = serializers.StringRelatedField(many= False)
    available_time = serializers.StringRelatedField(many= True)
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'image', 'designation', 'specialization', 'available_time', 'fee', 'meet_link']

    def get_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'