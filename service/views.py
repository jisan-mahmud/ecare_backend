from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ServiceSerializer
from .models import Service

class ServiceViewset(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer 