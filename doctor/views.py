from rest_framework import viewsets
from . import models
from .serializers import (
    DoctorSerializer,
    DesignationSerializer,
    SpecializationSerializer,
    AvailableTimeSerializer,
    ReviewSerializer
)

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = DoctorSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = DesignationSerializer

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = SpecializationSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer
