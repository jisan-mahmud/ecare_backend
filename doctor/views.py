from rest_framework import viewsets
from . import models
from .serializers import (
    DoctorSerializer,
    DesignationSerializer,
    SpecializationSerializer,
    AvailableTimeSerializer,
    ReviewSerializer
)
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'page_size'


class DoctorViewset(viewsets.ReadOnlyModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        if search is not None:
            search = search.strip()
            queryset = queryset.filter(
                Q(user__first_name__icontains=search) |
                Q(user__last_name__icontains=search) |
                Q(designation__name__icontains= search) |
                Q(specialization__name__icontains= search)
                ).distinct()
        return queryset



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
